import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Green Destinations AI", layout="wide")

# Custom CSS for premium look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌱 Green Destinations: Strategic Attrition Intelligence")
st.markdown("---")

# Load model
@st.cache_resource
def load_assets():
    if not os.path.exists("models/model_pipeline.pkl"):
        return None, None
    model = joblib.load("models/model_pipeline.pkl")
    background = pd.read_pickle("models/shap_background.pkl")
    return model, background

model, background = load_assets()

if model is None:
    st.error("❌ Model not found! Please run 'python src/train.py' first.")
    st.stop()

# Layout: Sidebar for inputs, Main for results
with st.sidebar:
    st.header("👤 Employee Profile")
    age = st.slider("Age", 18, 60, 30)
    dept = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
    income = st.number_input("Monthly Income ($)", 1000, 20000, 5000)
    overtime = st.selectbox("Overtime", ["Yes", "No"])
    total_years = st.slider("Total Working Years", 0, 40, 10)
    years_at_co = st.slider("Years at Company", 0, 40, 5)
    role = st.selectbox("Job Role", ["Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director", "Healthcare Representative", "Manager", "Sales Representative", "Research Director", "Human Resources"])
    
    # Minimal inputs for this demo (expandable)
    env_sat = st.slider("Environment Satisfaction", 1, 4, 3)
    job_sat = st.slider("Job Satisfaction", 1, 4, 3)

# Main Result Section
if st.button("Analyze Attrition Risk"):
    # Prepare input data
    input_data = {
        "Age": age,
        "Department": dept,
        "MonthlyIncome": income,
        "OverTime": overtime,
        "TotalWorkingYears": total_years,
        "YearsAtCompany": years_at_co,
        "JobRole": role,
        "EnvironmentSatisfaction": env_sat,
        "JobSatisfaction": job_sat,
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
    
    input_df = pd.DataFrame([input_data])
    
    # Feature Engineering
    input_df['IncomePerAge'] = input_df['MonthlyIncome'] / input_df['Age']
    input_df['TenureRatio'] = input_df['YearsAtCompany'] / (input_df['TotalWorkingYears'] + 1)
    
    # Prediction
    prob = model.predict_proba(input_df)[0][1]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Model Prediction")
        if prob >= 0.3:
            st.error(f"### High Risk: {prob*100:.1f}%")
            st.write("Targeted retention strategy required.")
        else:
            st.success(f"### Low Risk: {prob*100:.1f}%")
            st.write("Employee is likely to stay.")
            
    with col2:
        st.subheader("Explainable AI (SHAP)")
        # Explainability
        explainer = shap.TreeExplainer(model.named_steps['classifier'])
        transformed_data = model.named_steps['preprocessor'].transform(input_df)
        shap_values = explainer.shap_values(transformed_data)
        
        # Plot
        fig, ax = plt.subplots(figsize=(10, 8))
        feature_names = model.named_steps['preprocessor'].get_feature_names_out()
        shap.bar_plot(shap_values[1][0], feature_names=feature_names, max_display=10, show=False)
        plt.tight_layout()
        st.pyplot(fig)
        st.write("👆 Positive values (right) increase attrition risk, negative values (left) decrease it.")

st.markdown("---")
st.info("💡 **Tip for Recruiters:** This app demonstrates end-to-end ML integration, explainable AI (SHAP), and production-ready backend design.")
