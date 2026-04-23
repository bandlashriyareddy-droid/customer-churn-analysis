# Customer Churn Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# ---------------------------
# Data Cleaning
# ---------------------------

# Remove unnecessary column
df.drop("customerID", axis=1, inplace=True)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Remove missing values
df.dropna(inplace=True)

# Convert Churn to numeric (Yes = 1, No = 0)
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# ---------------------------
# Basic Analysis
# ---------------------------

# Total records
print("Total Customers:", len(df))

# Churn count
print("Churn Count:\n", df["Churn"].value_counts())

# ---------------------------
# Visualizations
# ---------------------------

# 1. Churn Distribution
plt.figure(figsize=(6,4))
sns.countplot(x="Churn", data=df)
plt.title("Churn Distribution")
plt.savefig("churn_distribution.png")
plt.close()

# 2. Contract vs Churn
plt.figure(figsize=(8,5))
sns.countplot(x="Contract", hue="Churn", data=df)
plt.title("Contract vs Churn")
plt.xticks(rotation=30)
plt.savefig("contract_vs_churn.png")
plt.close()

# 3. Monthly Charges vs Churn
plt.figure(figsize=(6,4))
sns.boxplot(x="Churn", y="MonthlyCharges", data=df)
plt.title("Monthly Charges vs Churn")
plt.savefig("monthly_charges_vs_churn.png")
plt.close()

print("Analysis complete. Graphs saved.")