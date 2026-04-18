# Problem 1: Customer Demographics vs Purchase Behavior
# Goal: Age aur gender ka purchase par impact

# Histogram (Age distribution)
# Bar chart (Gender vs Purchase)
# Boxplot (Age vs Purchase)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\games1\ecommerce_data.csv")

# Age Distribution
plt.figure()
sns.histplot(df['age'], kde=True)
plt.title("Age Distribution")
plt.show()

# Gender vs Purchase
plt.figure()
sns.countplot(x='gender', hue='purchase', data=df)
plt.title("Gender vs Purchase")
plt.show()

# Age vs Purchase
plt.figure()
sns.boxplot(x='purchase', y='age', data=df)
plt.title("Age vs Purchase")
plt.show()