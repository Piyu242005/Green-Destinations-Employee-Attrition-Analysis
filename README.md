<!-- HEADER -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=200&section=header&text=Employee%20Attrition%20Prediction%20System&fontSize=40&fontAlignY=35&fontColor=ffffff&desc=Green%20Destinations%20HR%20Analytics%20%7C%20AI-Powered%20Retention%20Insights&descAlignY=55&descAlign=50" width="100%"/>

</div>

# 🌍 Green Destinations Employee Attrition Analysis

> A comprehensive data science project analyzing employee turnover to identify key retention drivers for Green Destinations.

![Green Destinations Logo](greendestination+logo.png)

---

## 🛑 Problem Statement

Employee attrition is a critical challenge for modern businesses. High turnover rates not only incur significant recruitment and training costs but also disrupt team productivity, institutional knowledge, and overall morale. Understanding **why** employees leave and predicting **who** might leave next enables proactive HR strategies to improve retention and organizational stability.

---

## 🎯 Objectives

![Project Objective](Project%20Objective.jpg)

- **Calculate Attrition Rate:** Understand the overall employee turnover.
- **Identify Key Drivers:** Pinpoint the specific workplace factors (age, years at company, income) that contribute most to an employee's decision to leave.
- **Provide Actionable Insights:** Deliver data-driven recommendations to the HR department for improving employee retention.
- **Leverage AI Tools:** Use OPUS for enhanced exploratory analysis and documentation support.

---

## 📊 Dataset

The analysis is based on a comprehensive HR dataset containing **1,470 employee records**.

- **File:** `greendestination (1) (1).csv`
- **Features:** 35+ columns encompassing:
  - **Demographics:** Age, Gender
  - **Compensation:** Monthly Income
  - **Work Experience:** Years at Company, Total Working Years
  - **Work Environment:** OverTime, Environment Satisfaction

---

## 🛠️ Methodology

1. **✅ Data Cleaning & Preprocessing:** Handled missing values and structured data for analysis.
2. **📊 Exploratory Data Analysis (EDA):** Uncovered bivariate and multivariate relationships between HR metrics and attrition.
3. **📈 Attrition Rate Calculation:** Determined baseline turnover metrics.
4. **🔗 Factor Correlation Insights:** Analyzed key demographic and professional indicators.
5. **🤖 OPUS-Assisted Interpretation:** Used OPUS for insight generation and narrative framing.

---

## 📉 Visualizations & Screenshot Gallery

Here are the key steps and findings from the exploratory data analysis:

| Load and Explore Data | Calculate Attrition Rate |
| :---: | :---: |
| ![Load and Explore](Screenshot%20Gallery/1.%20Load%20and%20Explore%20the%20Data.png) | ![Attrition Rate](Screenshot%20Gallery/2.%20Calculate%20Attrition%20Rate.png) |

| Age vs Attrition | Years at Company vs Attrition |
| :---: | :---: |
| ![Age](Screenshot%20Gallery/3.%20Factor%20Analysis%20Age%20vs%20Attrition.png) | ![Years at Company](Screenshot%20Gallery/4.%20Factor%20Analysis%20Years%20at%20Company%20vs%20Attrition.png) |

| Monthly Income vs Attrition | Summary & Key Findings |
| :---: | :---: |
| ![Monthly Income](Screenshot%20Gallery/5.%20Factor%20Analysis%20Monthly%20Income%20vs%20Attrition.png) | ![Key Findings](Screenshot%20Gallery/6.%20Summary%20&%20Key%20Findings.png) |

*(See [Summary & Key Findings (2)](Screenshot%20Gallery/6.%20Summary%20&%20Key%20Findings%20(2).png) for additional insights.)*

---

## 📈 Results & Key Findings

### Overall Attrition Rate: **16.12%**

| Metric | Employees Who Left | Employees Who Stayed |
| :--- | :---: | :---: |
| **Average Age** | 33.6 years | 37.6 years |
| **Years at Company (avg)** | 5.1 years | 7.4 years |
| **Monthly Income (avg)** | $4,787 | $6,833 |

### ⚠️ High-Risk Groups Identified:
- **Age 18-25:** **35.8%** attrition rate
- **Tenure 0-2 years:** **29.8%** attrition rate
- **Monthly Income <$3K:** **28.6%** attrition rate

---

## 💡 Business Recommendations

1. **🎯 Focus on Young Employees (18-25):** Implement mentorship programs and career development initiatives to engage younger staff.
2. **📈 Retention for New Hires:** Create strong onboarding and engagement programs specifically targeting the first 2 years of employment.
3. **💵 Review Compensation:** Consider salary adjustments and competitive benchmarking for lower-income positions.
4. **🔍 Exit Interviews:** Conduct detailed exit interviews to understand the nuanced, specific reasons behind departures.

---

## 💻 Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn)
---

## 📂 Project Structure

```text
Green-Destinations-Employee-Attrition-Analysis/
│
├── README.md                       # Project documentation
├── CODE_OF_CONDUCT.md              # Community guidelines
├── GreenDestination.ipynb          # Main EDA and analysis notebook
├── greendestination (1) (1).csv    # Raw HR dataset
├── greendestination+logo.png       # Company logo
├── Project Objective.jpg           # Project objective image
└── Screenshot Gallery/             # Project visualizations and assets
```

---
<details>
  <summary> 🚀 How to Run</summary>

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Green-Destinations-Employee-Attrition-Analysis.git
   cd Green-Destinations-Employee-Attrition-Analysis
   ```

2. **Install dependencies:**
   Ensure Python 3.x is installed, then run:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

3. **Launch the Notebook:**
   Open the repository in VS Code or Jupyter Notebook, and run `GreenDestination.ipynb` to view or reproduce the analysis.

</details>
---

## 🔮 Future Improvements

- **Advanced Modeling:** Implement predictive Machine Learning algorithms (like Random Forest or XGBoost) to predict individual attrition risk.
- **Interactive Dashboard:** Develop an HR dashboard using Streamlit or Power BI for real-time tracking.

---

## Let's Connect & Collaborate

<div align="center">

[![Email](https://img.shields.io/badge/📧_Email-piyu.143247@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:piyu.143247@gmail.com)
[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-Piyush_Ramteke-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/piyush-ramteke-24-mylife)
[![Instagram](https://img.shields.io/badge/📸_Instagram-my.life__24143-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/my.life_24143/)

</div>

---
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=140&section=footer&text=Built%20by%20Piyush&fontSize=22&fontColor=e0d7ff&fontAlignY=70&fontAlign=50" width="100%"/>

[![GitHub](https://img.shields.io/badge/Follow%20%40Piyu242005-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Piyu242005)

**Found this useful? Give it a** ⭐ **— it really helps!**

![Visitors](https://api.visitorbadge.io/api/visitors?path=Piyu242005%2FGreen-Destinations-Employee-Attrition-Analysis&countColor=%23c8ff00)

</div>