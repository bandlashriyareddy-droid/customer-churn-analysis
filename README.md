# 📊 Customer Churn Analysis

## 🔍 Overview
This project analyzes customer churn behavior using Python and Power BI to identify key factors affecting customer retention.

## 🛠 Tools & Technologies
- Python (Pandas, Matplotlib, Seaborn)
- Power BI
- CSV Dataset (Telco Customer Churn)

## 📁 Dataset
- Total Records: 7,043 customers
- Features: Demographics, services, billing, tenure
- Target Variable: Churn (Yes = 1, No = 0)

## ⚙️ Project Workflow
1. Data Cleaning
   - Removed unnecessary columns
   - Handled missing values
   - Converted data types

2. Data Analysis (EDA)
   - Churn distribution
   - Contract vs churn
   - Monthly charges vs churn

3. Visualization
   - Built charts using Seaborn
   - Created Power BI dashboard

## 📊 Key Insights
- 📌 Customers with **month-to-month contracts** churn the most
- 📌 Higher **monthly charges** increase churn probability
- 📌 Long-term contracts reduce churn
- 📌 Overall churn rate ≈ **26.5%**

## 📸 Project Files
- churn_analysis.py → Data cleaning & analysis
- churn_distribution.png → Churn distribution
- contractvschurn.png → Contract vs churn
- monthlychargesvschurn.png → Monthly charges vs churn
- Basic Power BI dashboard.png → Dashboard screenshot

## 🎯 Outcome
This project helps identify customer segments with high churn risk and supports data-driven decision-making for improving retention strategies.

## 🚀 Future Improvements
- Add churn rate KPI in Power BI
- Build predictive model using machine learning
- Enhance dashboard interactivity
