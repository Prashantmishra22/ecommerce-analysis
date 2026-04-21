
# Problem 1: Customer Demographics Impact on Purchase Behavior
# Age Distibution (Histogram)
# Gender vs Purchase (Bar Chart)


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\games1\ecommerce_data.csv")

plt.figure()
plt.boxplot(df['age'])
plt.title("Boxplot for Age (Outlier Detection)")
plt.ylabel("Age")
plt.show()

Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_clean = df[(df['age'] >= lower_bound) & (df['age'] <= upper_bound)]

plt.figure()
plt.hist(df_clean['age'], bins=20)
plt.title("Age Distribution (After Removing Outliers)")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

group = df_clean.groupby('gender')['purchase'].mean()

plt.figure()
group.plot(kind='bar')
plt.title("Gender vs Purchase Rate (Cleaned Data)")
plt.xlabel("Gender")
plt.ylabel("Purchase Rate")
plt.show()