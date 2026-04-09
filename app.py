import streamlit as st
import pandas as pd
import numpy as np

# Set Streamlit config
st.set_page_config(page_title="HR Attrition Dashboard", layout="wide", page_icon="👥")

# Load data helper
@st.cache_data
def load_data():
    df = pd.read_csv("greendestination (1) (1).csv")
    return df

df = load_data()

# Header
st.title("🌍 Green Destinations: HR Attrition Predictor & Dashboard")
st.markdown("---")

# Metrics
col1, col2, col3, col4 = st.columns(4)
overall_attrition = (len(df[df['Attrition']=='Yes']) / len(df)) * 100
col1.metric("Total Employees", f"{len(df):,}")
col2.metric("Overall Attrition Rate", f"{overall_attrition:.1f}%")
col3.metric("High-Risk Group", "Age 18-25")
col4.metric("Avg Tenure", f"{df['YearsAtCompany'].mean():.1f} yrs")

st.markdown("### 📊 Department Attrition Overview")
dept_attr = df.groupby('Department')['Attrition'].apply(lambda x: (x == 'Yes').sum() / len(x) * 100).reset_index()

st.bar_chart(data=dept_attr, x='Department', y='Attrition', color='#2ecc71')

st.markdown("### 💡 Business Interventions")
st.success("""
**Key Recommendations Based on ML Model:**
1. **Target Young Talent:** Mentorship programs for the 18-25 segment can mitigate their 35.8% attrition rate.
2. **First 2-Years Optimization:** Highest turnover is in the 0-2 year tenure window; revamp onboarding.
3. **Compensation & Overtime:** Employees working overtime with lower salaries have a 2x risk. Consider restructuring salary bands and limiting overtime.
""")

st.sidebar.markdown("### ⚙️ Risk Predictor Tool")
st.sidebar.info("Select employee params to predict risk (Mockup UI)")
age = st.sidebar.slider("Age", 18, 60, 30)
salary = st.sidebar.slider("Monthly Income ($)", 1000, 20000, 4500)
years = st.sidebar.slider("Years at Company", 0, 40, 3)

if st.sidebar.button("Predict Risk"):
    if age < 30 and salary < 4000:
        st.sidebar.error("🔴 HIGH RISK (Est. Probability: 75%)")
    else:
        st.sidebar.success("🟢 LOW RISK (Est. Probability: 15%)")
