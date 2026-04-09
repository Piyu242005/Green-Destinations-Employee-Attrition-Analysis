import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline
import os

def train_and_save_model():
    print("Loading HR dataset...")
    # Load data
    df = pd.read_csv("greendestination (1) (1).csv")
    
    # 1. Select features
    # Using key drivers identified in previous EDA
    features = ['Age', 'MonthlyIncome', 'YearsAtCompany', 'OverTime']
    X = df[features]
    
    # Target variable - Convert 'Yes'/'No' to 1/0
    y = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)
    
    # 2. Build preprocessing pipeline
    # Scale numerical features, encode categorical features
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['Age', 'MonthlyIncome', 'YearsAtCompany']),
            ('cat', OneHotEncoder(drop='first'), ['OverTime']) # 'No'->0, 'Yes'->1
        ])
        
    # 3. Create the modeling pipeline with SMOTE
    # SMOTE handles the class imbalance by creating synthetic examples of the minority class (Attrition)
    pipeline = ImbPipeline([
        ('preprocessor', preprocessor),
        ('smote', SMOTE(random_state=42)),
        ('classifier', RandomForestClassifier(n_estimators=150, max_depth=10, random_state=42))
    ])
    
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    print("Training Random Forest model with SMOTE...")
    pipeline.fit(X_train, y_train)
    
    # Evaluate and print metrics
    train_acc = pipeline.score(X_train, y_train)
    test_acc = pipeline.score(X_test, y_test)
    print(f"✅ Training Accuracy: {train_acc:.2%}")
    print(f"✅ Testing Accuracy: {test_acc:.2%}")
    
    # 4. Save the trained pipeline as 'model.pkl'
    model_path = "model.pkl"
    joblib.dump(pipeline, model_path)
    print(f"🎉 Model successfully trained and saved to: {model_path}")

if __name__ == "__main__":
    train_and_save_model()