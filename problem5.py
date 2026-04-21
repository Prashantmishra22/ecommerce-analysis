# Hypothesis Testing (Gender vs Purchase)
# Goal: Gender ka purchase par effect test karna
#“Statistical Hypothesis Testing to Determine the Effect of Gender on Purchase Behavior”


import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"D:\games1\ecommerce_data.csv")

# Separate groups
male = df[df['gender'] == 'Male']['purchase']
female = df[df['gender'] == 'Female']['purchase']

# Basic stats
mean1 = male.mean()
mean2 = female.mean()

std1 = male.std(ddof=1)
std2 = female.std(ddof=1)

n1 = len(male)
n2 = len(female)

# Two-sample t-test
t_stat, p_value = stats.ttest_ind(male, female, equal_var=True)

# Degree of freedom
dfree = n1 + n2 - 2

# t-critical value
alpha = 0.05
t_critical = stats.t.ppf(1 - alpha/2, dfree)

# Output
print("----- Basic Statistics -----")
print(f"Male Mean: {mean1:.3f}")
print(f"Female Mean: {mean2:.3f}")
print(f"Male Std Dev: {std1:.3f}")
print(f"Female Std Dev: {std2:.3f}")
print(f"Sample Size Male: {n1}")
print(f"Sample Size Female: {n2}")

print("\n----- T-Test Results -----")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")
print(f"Degrees of Freedom: {dfree}")
print(f"T-Critical Value: {t_critical:.4f}")

# Decision
if p_value < alpha:
    print("\nConclusion: Reject H0 (Significant difference)")
else:
    print("\nConclusion: Fail to Reject H0 (No significant difference)")

# -------------------------
# GRAPH (IMPORTANT)
# -------------------------

# Purchase rate by gender
df.groupby('gender')['purchase'].mean().plot(kind='bar')

plt.title("Purchase Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Purchase Rate")

plt.show()