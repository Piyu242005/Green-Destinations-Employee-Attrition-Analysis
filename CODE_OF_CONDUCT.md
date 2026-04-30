# 🌍 Project Summary & Execution Guide

Here is a **short, simple, and easy-to-understand explanation** of this system:

---

### 📊 Project Explanation (Simple)

**Green Destinations Employee Attrition Analysis** is a smart tool that helps companies understand **why employees leave** and **who might leave next**.

It analyzes data like:
*   **Workload:** Are they working too much overtime?
*   **Pay:** Is their salary lower than others in similar roles?
*   **Experience:** How many years have they been with the company?
*   **Satisfaction:** Are they happy with their work environment?

**The Result:** It gives HR a "Risk Score" for each employee and explains the specific reasons for that risk, helping the company keep its best people.

---

### 🚀 How to Run the Project

To see the project in action, follow these steps:

#### 1. Start the Backend (API)
Open a terminal and run:
```bash
python -m uvicorn app.api:app --reload
```
*This starts the "brain" of the project that handles the math and predictions.*

#### 2. Start the Frontend (Dashboard)
Open a **second terminal** and run:
```bash
python -m streamlit run app/main.py
```
*This opens the visual dashboard in your web browser where you can interact with the data.*

---

### 🛠️ Technical Setup (First Time Only)

If you haven't installed the requirements yet, run:
```bash
pip install -r requirements.txt
```

To retrain the model with fresh data:
```bash
python src/train.py
```