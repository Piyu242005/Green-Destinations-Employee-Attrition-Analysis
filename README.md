# Employee Attrition Analysis using OPUS

![Green Destinations Logo](greendestination+logo.png)

## Project Objective

![Project Objective](Project%20Objective.jpg)

## Overview

This project analyzes employee attrition for **Green Destinations** to identify patterns and potential risk factors. The dataset contains employee details such as age, income, and years at the company. OPUS is used to assist with data summarization, insight generation, and report formatting.

---

## Objectives

1. Calculate overall attrition rate
2. Identify key factors influencing attrition (age, years at company, income)
3. Provide actionable HR insights supported by data
4. Use OPUS for enhanced exploratory analysis and documentation support

---

## Key Features

- ✅ Data cleaning and preprocessing
- 📊 Exploratory data analysis (EDA)
- 📈 Attrition rate calculation
- 🔗 Factor correlation insights
- 📉 Visualization of important trends
- 🤖 OPUS-assisted interpretation and reporting

---

## Tools & Technologies

| Category | Tools |
|----------|-------|
| **Programming** | Python 3.x |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn (optional) |
| **AI Assistant** | OPUS for narrative and documentation enhancement |

---

## Dataset

- **File:** `greendestination (1) (1).csv`
- **Records:** 1,470 employees
- **Features:** 35 columns including Age, Attrition, MonthlyIncome, YearsAtCompany, etc.

---

## Expected Outcomes

| Outcome | Description |
|---------|-------------|
| 📊 **Attrition Rate** | Clear understanding of overall employee turnover (16.12%) |
| 👤 **Risk Profiles** | Insight into high-risk employee demographics |
| 💡 **HR Support** | Data-driven decision support for retention strategies |

---

## Key Findings

### Overall Attrition Rate: **16.12%**

| Factor | Employees Who Left | Employees Who Stayed |
|--------|-------------------|---------------------|
| **Age (avg)** | 33.6 years | 37.6 years |
| **Years at Company (avg)** | 5.1 years | 7.4 years |
| **Monthly Income (avg)** | $4,787 | $6,833 |

### High-Risk Groups
- 🔴 Age 18-25: 35.8% attrition rate
- 🔴 Tenure 0-2 years: 29.8% attrition rate
- 🔴 Income <$3K: 28.6% attrition rate

---

## Recommendations

1. **🎯 Focus on Young Employees (18-25):** Implement mentorship programs and career development initiatives
2. **📈 Retention for New Hires:** Create strong onboarding and engagement programs for first 2 years
3. **💵 Review Compensation:** Consider salary adjustments for lower-income positions
4. **🔍 Exit Interviews:** Conduct detailed exit interviews to understand specific departure reasons

---

## Project Structure

```
Green Destinations/
├── README.md                       # Project documentation
├── GreenDestination.ipynb          # Main analysis notebook
├── greendestination (1) (1).csv    # Employee survey data
├── greendestination+logo.png       # Company logo
└── Project Objective.jpg           # Project objective image
```

---

## How to Run

1. Clone or download this repository
2. Ensure Python 3.x is installed with required packages:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
3. Open `GreenDestination.ipynb` in Jupyter Notebook or VS Code
4. Run all cells to reproduce the analysis

---

## Author

Analysis performed by **Piyu** with OPUS AI assistance for Green Destinations HR Department

---

## License

This project is for educational and internal HR analysis purposes.
