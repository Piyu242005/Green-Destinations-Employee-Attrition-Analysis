import pandas as pd

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies shared feature engineering logic for both training and serving.
    """
    df = df.copy()
    
    # Calculate Income Per Age
    if 'MonthlyIncome' in df.columns and 'Age' in df.columns:
        df['IncomePerAge'] = df['MonthlyIncome'] / df['Age']
        
    # Calculate Tenure Ratio
    if 'YearsAtCompany' in df.columns and 'TotalWorkingYears' in df.columns:
        df['TenureRatio'] = df['YearsAtCompany'] / (df['TotalWorkingYears'] + 1)
        
    return df
