<!-- Animated Header -->
<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=30&pause=1000&color=2E8B57&center=true&vCenter=true&width=800&height=60&lines=Employee+Attrition+Machine+Learning;Data-Driven+HR+Insights;Green+Destinations" alt="Typing SVG" />
</div>

# 🌍 Green Destinations Employee Attrition System

> A job-ready Machine Learning and Business Intelligence project turning raw HR data into **actionable retention strategies**. Not just graphs—a complete decision-making HR engine.

---

## 🛑 1. Problem Statement & Business Context

Employee attrition is a massive hidden cost for modern businesses. High turnover rates incur significant recruitment, onboarding, and training costs while disrupting team productivity. 

**Our Goal:** Move beyond guessing. We need to predict **who** is likely to leave and understand exactly **why** so that HR can deploy targeted, data-backed interventions to save money and retain top talent.

---

## 📊 2. The Dataset

The analysis is based on a comprehensive HR dataset containing **1,470 employee records**, mapping directly to key organizational pillars:

- **Demographics:** Age, Gender
- **Compensation & Roles:** Monthly Income, Job Level, Department
- **Work Experience:** Years at Company, Total Working Years
- **Work Environment:** OverTime, Environment Satisfaction

---

## 🔍 3. Exploratory Data Analysis (EDA)

Before building predictive models, a deep-dive EDA revealed our baseline metrics and high-risk segments.

### Key Metrics Uncovered
- **Overall Attrition Rate:** 16.12%
- **Average Tenure for Leavers:** 5.1 Years (vs 7.4 for Stayers)
- **High-Risk Segment 1:** Employees aged 18-25 (35.8% attrition rate)
- **High-Risk Segment 2:** Tenure 0-2 years (29.8% attrition rate)
- **High-Risk Segment 3:** Monthly Income <$3K (28.6% attrition rate)

*(Insights derived from Python Pandas, Seaborn & Matplotlib visualizations inside the primary notebook).*

---

## ⚙️ 4. Feature Engineering & Class Imbalance

Attrition data is notoriously imbalanced (only ~16% of employees leave). We applied rigorous Data Science techniques to prepare the data:

1. **One-Hot Encoding** for categorical features.
2. **StandardScaling** for numeric variable normalization.
3. **SMOTE (Synthetic Minority Over-sampling Technique)** applied to handle the 84:16 class imbalance, ensuring our models don't just predict "No" for everyone.

---

## 🧠 5. Machine Learning Models

We modeled the data to predict attrition using state-of-the-art algorithms:

### Random Forest Classifier
- A robust ensemble method that performed excellently off-the-shelf.
- Provided high interpretability via `feature_importances_`.
- **Accuracy:** Tested & Optimized via Train/Test Splits.
- Evaluated via precision, recall, and a **Confusion Matrix** to understand false positives vs. false negatives.

### Logistic Regression
- Used as an interpretable baseline model to measure the linear bounds of our feature set.

**(Results and Feature Importance charts are documented in `GreenDestination.ipynb`)**

---

## 📈 6. Results & Model Interpretation

By extracting the Feature Importance from the Random Forest, the model literally tells us **why** employees leave:

1. **Monthly Income:** Lower brackets are vastly more likely to quit.
2. **OverTime:** Employees working consistent overtime show significantly higher burnout.
3. **Age & Tenure:** Junior staff in their first 2 years are the most volatile.

> *"Employees with a low salary combined with high overtime have functionally double the attrition risk."*

---

## 🎯 7. Strong Business Recommendations

Insights without action are useless. Based on the ML Model, the recommended HR strategy is:

**1. Target the 18-25 Segment & New Hires (0-2 Years)**  
Revamp the 90-day onboarding window. Assign senior mentors to younger staff immediately to increase early engagement.

**2. Restructure Compensation & Limit OverTime**  
The model explicitly flags OverTime + Low Salary as a toxic combination. Run an audit on entry-level compensation bands and forcibly cap weekly overtime hours for high-risk individuals.

**3. Conduct Targeted 'Stay Interviews'**  
Use the predictive model to flag top performers at >60% risk. Hold proactive "stay interviews" with them *before* they resign.

---

## 🌐 8. Interactive Streamlit Dashboard

To make this useful for non-technical recruiters and HR Managers, a live **HR Attrition Dashboard** was developed.

### Features:
- Filter attrition rates by department.
- Real-time **Risk Predictor Tool** allowing HR to plug in employee parameters (Age, Salary, Tenure) to get an instant % risk assessment.

> Run the dashboard locally: `streamlit run app.py`

---

## 💻 9. Tech Stack & Project Structure

- **Data Manipulation & Viz:** Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning Analysis:** Scikit-Learn, Imbalanced-Learn (SMOTE)
- **Web App UI:** Streamlit

```text
Green-Destinations-Employee-Attrition-Analysis/
│
├── README.md                       # Project documentation
├── app.py                          # Streamlit Interactive Dashboard
├── GreenDestination.ipynb          # Advanced ML & EDA Notebook
└── greendestination (1) (1).csv    # Raw HR dataset
```

---

## 🚀 10. How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Green-Destinations-Employee-Attrition-Analysis.git
   cd Green-Destinations-Employee-Attrition-Analysis
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn streamlit
   ```

3. **Launch the ML Notebook:**
   ```bash
   jupyter notebook GreenDestination.ipynb
   ```

4. **Launch the HR Dashboard:**
   ```bash
   streamlit run app.py
   ```

---

## 📧 Let's Connect & Collaborate

<div align="center">

[![Email](https://img.shields.io/badge/📧_Email-piyu.143247@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:piyu.143247@gmail.com)
[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-Piyush_Ramteke-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/piyush-ramteke-24-mylife)
[![GitHub](https://img.shields.io/badge/🐙_GitHub-Piyu242005-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Piyu242005)
[![Instagram](https://img.shields.io/badge/📸_Instagram-my.life__24143-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/my.life_24143/)

</div>

---

<div align="center">

### ⭐ If you find this repository helpful, dropping a star would mean a lot!

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%" />

Made with 💚 by **Piyush Ramteke** © 2026

![Visitors](https://api.visitorbadge.io/api/visitors?path=Piyu242005%2FPiyu-Portfolio-Website&countColor=%23c8ff00)

</div>
