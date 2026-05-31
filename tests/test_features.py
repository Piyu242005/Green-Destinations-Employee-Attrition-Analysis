import pandas as pd
import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.features import engineer_features

def test_engineer_features_income_per_age():
    df = pd.DataFrame({
        'MonthlyIncome': [5000, 10000],
        'Age': [25, 50]
    })
    
    result = engineer_features(df)
    
    assert 'IncomePerAge' in result.columns
    assert result['IncomePerAge'].iloc[0] == 200.0
    assert result['IncomePerAge'].iloc[1] == 200.0

def test_engineer_features_tenure_ratio():
    df = pd.DataFrame({
        'YearsAtCompany': [5, 10],
        'TotalWorkingYears': [9, 19]
    })
    
    result = engineer_features(df)
    
    assert 'TenureRatio' in result.columns
    assert result['TenureRatio'].iloc[0] == 0.5  # 5 / (9 + 1)
    assert result['TenureRatio'].iloc[1] == 0.5  # 10 / (19 + 1)

def test_engineer_features_missing_columns():
    df = pd.DataFrame({
        'SomeColumn': [1, 2]
    })
    
    result = engineer_features(df)
    
    # Should silently pass and return original dataframe without errors
    assert 'IncomePerAge' not in result.columns
    assert 'TenureRatio' not in result.columns
    assert len(result.columns) == 1
