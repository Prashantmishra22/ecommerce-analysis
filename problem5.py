# Hypothesis Testing (Gender vs Purchase)

# Goal: Gender ka purchase par effect test karna
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
df = pd.read_csv("D:\games1\ecommerce_data.csv")
male = df[df['gender'] == 'Male']['purchase']
female = df[df['gender'] == 'Female']['purchase']

t_stat, p_value = ttest_ind(male, female)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# Visualization
plt.figure()
sns.boxplot(x='gender', y='purchase', data=df)
plt.title("Gender vs Purchase")
plt.show()

plt.figure()
sns.barplot(x='gender', y='purchase', data=df)
plt.title("Purchase Rate by Gender")
plt.show()