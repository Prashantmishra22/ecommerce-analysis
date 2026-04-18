# Hypothesis Testing (Gender vs Purchase)

# Goal: Gender ka purchase par effect test karna
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, norm
import numpy as np

df = pd.read_csv(r"D:\games1\ecommerce_data.csv")
male = df[df['gender'] == 'Male']['purchase']
female = df[df['gender'] == 'Female']['purchase']

# T-test
t_stat, t_p = ttest_ind(male, female)

# Z-test
mean1, mean2 = male.mean(), female.mean()
std1, std2 = male.std(), female.std()
n1, n2 = len(male), len(female)

se = np.sqrt((std1**2/n1) + (std2**2/n2))
z_stat = (mean1 - mean2) / se
z_p = 2 * (1 - norm.cdf(abs(z_stat)))

print("T-test p-value:", t_p)
print("Z-test p-value:", z_p)

# Boxplot
import matplotlib.pyplot as plt

# Purchase rate by gender
df.groupby('gender')['purchase'].mean().plot(kind='bar')

plt.title("Purchase Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Purchase Rate")
plt.show()