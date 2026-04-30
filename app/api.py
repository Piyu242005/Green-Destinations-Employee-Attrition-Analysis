from fastapi import FastAPI
import joblib
import pandas as pd
import uvicorn

app = FastAPI(
    title="Green Destinations Employee Attrition API",
    description="API to predict the probability of employee attrition.",
    version="1.0.0"
)

# Load the trained pipeline
try:
    model = joblib.load("models/model_pipeline.pkl")
except:
    model = None

@app.get("/")
def home():
    return {
        "message": "Attrition Prediction API is active and running successfully.",
        "developer": "Piyush Ramteke",
        "role": "Data Scientist | AI/ML Engineer",
        "status": "Ready to serve predictions" if model else "Model Not Found"
    }

@app.post("/predict")
def predict(data: dict):
    if not model:
        return {"error": "Model not loaded"}
    
    # Convert incoming JSON to DataFrame
    input_df = pd.DataFrame([data])
    
    # Apply same feature engineering as training
    input_df['IncomePerAge'] = input_df['MonthlyIncome'] / input_df['Age']
    input_df['TenureRatio'] = input_df['YearsAtCompany'] / (input_df['TotalWorkingYears'] + 1)
    
    # Get probability
    prob = model.predict_proba(input_df)[0][1]
    
    # Prediction based on tuned threshold
    threshold = 0.3
    risk_level = "High" if prob >= threshold else "Low"
    
    return {
        "attrition_probability": round(float(prob), 2),
        "risk_level": risk_level,
        "tuned_threshold": threshold,
        "action": "Immediate retention interview suggested" if risk_level == "High" else "Monitor satisfaction"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
