from fastapi.testclient import TestClient
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.api import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "status" in response.json()

def test_predict_endpoint():
    # Construct a payload resembling the real one
    payload = {
        "Age": 30,
        "Department": "Sales",
        "MonthlyIncome": 5000,
        "OverTime": "Yes",
        "TotalWorkingYears": 5,
        "YearsAtCompany": 2,
        "JobRole": "Sales Executive",
        "EnvironmentSatisfaction": 3,
        "JobSatisfaction": 3,
        "MonthlyRate": 14313,
        "DailyRate": 802,
        "HourlyRate": 66,
        "BusinessTravel": "Travel_Rarely",
        "DistanceFromHome": 5,
        "Education": 3,
        "EducationField": "Life Sciences",
        "Gender": "Male",
        "JobInvolvement": 3,
        "JobLevel": 2,
        "MaritalStatus": "Single",
        "NumCompaniesWorked": 1,
        "PercentSalaryHike": 15,
        "PerformanceRating": 3,
        "RelationshipSatisfaction": 3,
        "StockOptionLevel": 0,
        "TrainingTimesLastYear": 3,
        "WorkLifeBalance": 3,
        "YearsInCurrentRole": 2,
        "YearsSinceLastPromotion": 1,
        "YearsWithCurrManager": 2
    }
    
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    
    data = response.json()
    assert "attrition_probability" in data
    assert "risk_level" in data
    assert "tuned_threshold" in data
