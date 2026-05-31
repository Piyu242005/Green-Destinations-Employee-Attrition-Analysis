import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report, roc_auc_score

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import config
from src.features import engineer_features

def build_advanced_pipeline(X):
    """Builds an ML pipeline with preprocessing and resampling."""
    num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = X.select_dtypes(include=['object']).columns.tolist()

    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
    ])

    pipeline = ImbPipeline([
        ('preprocessor', preprocessor),
        ('smote', SMOTE(random_state=config.RANDOM_STATE)),
        ('classifier', RandomForestClassifier(random_state=config.RANDOM_STATE))
    ])
    return pipeline

def train_and_save():
    print("Loading data...")
    df = pd.read_csv(config.DATA_PATH)
    
    print("Engineering features...")
    df = engineer_features(df)
    
    # Drop non-predictive columns
    X = df.drop(['Attrition', 'EmployeeCount', 'Over18', 'StandardHours', 'EmployeeNumber'], axis=1)
    y = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config.TEST_SIZE, stratify=y, random_state=config.RANDOM_STATE
    )

    print("Training model with SMOTE and Random Forest...")
    print("Performing GridSearchCV...")
    pipeline = build_advanced_pipeline(X)
    
    cv = StratifiedKFold(n_splits=config.CV_SPLITS, shuffle=True, random_state=config.RANDOM_STATE)
    
    grid_search = GridSearchCV(
        pipeline, 
        param_grid=config.RF_PARAM_GRID, 
        cv=cv, 
        scoring='recall', # Optimize for Recall
        n_jobs=-1,
        verbose=1
    )
    
    grid_search.fit(X_train, y_train)
    
    print(f"Best parameters found: {grid_search.best_params_}")
    best_model = grid_search.best_estimator_

    # Threshold Tuning for Recall (Recruiters want high Recall in Attrition)
    probs = best_model.predict_proba(X_test)[:, 1]
    
    y_pred_tuned = (probs >= config.MODEL_THRESHOLD).astype(int)
    
    print(f"\n--- Model Performance (Threshold: {config.MODEL_THRESHOLD}) ---")
    print(classification_report(y_test, y_pred_tuned))
    print(f"ROC-AUC Score: {roc_auc_score(y_test, probs):.4f}")

    # Ensure models directory exists
    os.makedirs(os.path.dirname(config.MODEL_PIPELINE_PATH), exist_ok=True)

    joblib.dump(best_model, config.MODEL_PIPELINE_PATH)
    print(f"\nPipeline saved to {config.MODEL_PIPELINE_PATH}")
    
    # Save training sample for SHAP explanations
    X_train.head(100).to_pickle(config.SHAP_BACKGROUND_PATH)

if __name__ == "__main__":
    train_and_save()
