import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report, roc_auc_score

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
        ('smote', SMOTE(random_state=42)),
        ('classifier', RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42))
    ])
    return pipeline

def train_and_save():
    print("Loading data...")
    df = pd.read_csv("data/greendestination (1) (1).csv")
    
    print("Engineering features...")
    # New features for better signal
    df['IncomePerAge'] = df['MonthlyIncome'] / df['Age']
    df['TenureRatio'] = df['YearsAtCompany'] / (df['TotalWorkingYears'] + 1)
    
    # Drop non-predictive columns
    X = df.drop(['Attrition', 'EmployeeCount', 'Over18', 'StandardHours', 'EmployeeNumber'], axis=1)
    y = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    print("Training model with SMOTE and Random Forest...")
    pipeline = build_advanced_pipeline(X)
    pipeline.fit(X_train, y_train)

    # Threshold Tuning for Recall (Recruiters want high Recall in Attrition)
    probs = pipeline.predict_proba(X_test)[:, 1]
    # We use a lower threshold (0.3 instead of 0.5) to catch more people likely to leave
    threshold = 0.3
    y_pred_tuned = (probs >= threshold).astype(int)
    
    print(f"\n--- Model Performance (Threshold: {threshold}) ---")
    print(classification_report(y_test, y_pred_tuned))
    print(f"ROC-AUC Score: {roc_auc_score(y_test, probs):.4f}")

    # Ensure models directory exists
    if not os.path.exists("models"):
        os.makedirs("models")

    model_path = "models/model_pipeline.pkl"
    joblib.dump(pipeline, model_path)
    print(f"\nPipeline saved to {model_path}")
    
    # Save training sample for SHAP explanations
    X_train.head(100).to_pickle("models/shap_background.pkl")

if __name__ == "__main__":
    train_and_save()
