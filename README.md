<!-- HEADER -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=200&section=header&text=Employee%20Attrition%20Prediction%20System&fontSize=40&fontAlignY=35&fontColor=ffffff&desc=Green%20Destinations%20HR%20Analytics%20%7C%20AI-Powered%20Retention%20Insights&descAlignY=55&descAlign=50" width="100%"/>

</div>

# 🌍 Green Destinations Employee Attrition Analysis

> **Production-Ready ML System** for predicting employee turnover with high recall and model explainability (SHAP).

![Green Destinations Logo](greendestination+logo.png)

---

## 🛑 Problem Statement

Employee attrition is a critical challenge for modern businesses. High turnover rates not only incur significant recruitment and training costs but also disrupt team productivity. This project delivers a **Strategic HR Intelligence System** that doesn't just predict "who" might leave, but explains **"why"** using Explainable AI (SHAP), allowing for targeted interventions.

---

## 🏗️ System Architecture

This project has been evolved from a simple notebook into a modular, production-grade architecture:

```mermaid
graph LR
    User((User)) --> UI[Streamlit Frontend]
    UI --> API[FastAPI Backend]
    API --> Model[Random Forest Pipeline]
    Model --> Prediction[Attrition Risk Score]
    Model --> XAI[SHAP Explainability]
    Prediction --> UI
    XAI --> UI
```

- **Backend (FastAPI):** A high-performance REST API for model serving.
- **Frontend (Streamlit):** An interactive dashboard for HR managers to perform "What-If" analysis.
- **ML Pipeline:** Robust preprocessing with `ColumnTransformer` and `ImbPipeline` to prevent data leakage.
- **Explainable AI (XAI):** Integrated SHAP plots to provide prediction transparency.

---

## 📊 Model Performance

We implemented a **Random Forest Classifier** optimized via a threshold search to prioritize **Recall**.

| Metric | Score | Note |
| :--- | :---: | :--- |
| **ROC-AUC** | **0.801** | Strong discriminative power |
| **Recall (Leaving Class)** | **0.66** | Optimized to catch 66% of leavers |
| **Precision** | **0.40** | Focused on coverage over exactness |
| **F1-Score** | **0.50** | Balanced for imbalanced classes |

✅ **Optimization:** We tuned the classification threshold to **0.3** (down from 0.5) to minimize **False Negatives**, ensuring fewer at-risk employees are missed by HR.

---

## 🚀 API Usage (Production Serving)

The model is served via a **FastAPI** microservice.

**Endpoint:** `POST /predict`

**Example Request:**
```json
{
  "Age": 30,
  "MonthlyIncome": 5000,
  "OverTime": "Yes",
  "TotalWorkingYears": 5,
  "YearsAtCompany": 2,
  "Department": "Sales",
  "JobRole": "Sales Executive"
}
```

**Example Response:**
```json
{
  "attrition_probability": 0.72,
  "risk_level": "High",
  "recommendation": "Urgent Stay Interview recommended"
}
```

---

## 📊 Dataset & Features

The analysis is based on a comprehensive HR dataset containing **1,470 employee records**.

- **File:** `data/greendestination (1) (1).csv`
- **Key Engineered Features:**
  - `IncomePerAge`: Monthly income normalized by age.
  - `TenureRatio`: Ratio of tenure at company vs. total career length.
  - `OverTime`: Binary indicator of workload pressure.

---

## 📉 Visualizations & Explainability

### 🔍 Model Explainability (SHAP)
We use **SHAP (SHapley Additive exPlanations)** to break down individual risk scores. This enables HR to understand the exact factors contributing to a "High Risk" prediction for a specific employee.

### 🖥️ System Interface Gallery

| FastAPI Backend Service | Upgraded Streamlit Dashboard |
| :---: | :---: |
| ![FastAPI Backend](Screenshot%20Gallery/FastAPI%20backend.png) | ![Streamlit Dashboard](Screenshot%20Gallery/Streamlit%20dashboard.png) |

---

## 💻 Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white)

---

## 📂 Project Structure

```text
Green-Destinations-Employee-Attrition-Analysis/
│
├── data/               # Raw HR dataset (CSV)
├── models/             # Serialized .pkl files (Pipeline & SHAP background)
├── src/                # Core ML Logic
│   └── train.py        # Optimized training script with threshold tuning
├── app/                # Deployment Layer
│   ├── api.py          # FastAPI REST Backend
│   └── main.py         # Streamlit XAI Frontend
├── requirements.txt    # Production dependencies
└── Dockerfile          # Containerization for deployment
```

---

<details>
  <summary> 🚀 How to Run (Development)</summary>

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Model
```bash
python src/train.py
```

### 3. Start Backend (FastAPI)
```bash
python -m uvicorn app.api:app --reload
```

### 4. Start Frontend (Streamlit)
```bash
streamlit run app/main.py
```

</details>

---

<details>
  <summary> 🐳 How to Run (Docker)</summary>

```bash
docker build -t attrition-system .
docker run -p 8000:8000 -p 8501:8501 attrition-system
```

</details>

---

## 🔮 Future Improvements

- **CI/CD Integration:** Automated model retraining via GitHub Actions.
- **Model Monitoring:** Implement tracking for data drift over time.
- **Prescriptive Analytics:** Suggesting specific retention actions (e.g., "Proposed 5% salary hike reduces risk by 15%").

---

## Let's Connect & Collaborate

<div align="center">

[![Email](https://img.shields.io/badge/📧_Email-piyu.143247@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:piyu.143247@gmail.com)
[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-Piyush_Ramteke-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/piyush-ramteke-24-mylife)

</div>

---
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=140&section=footer&text=Built%20by%20Piyush&fontSize=22&fontColor=e0d7ff&fontAlignY=70&fontAlign=50" width="100%"/>

[![GitHub](https://img.shields.io/badge/Follow%20%40Piyu242005-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Piyu242005)

</div>