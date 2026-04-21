
# Goal: Complete data understanding#
# “Comprehensive Analysis of Factors Influencing Purchase Behavior Using Data Visualization”

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (FIXED PATH)
df = pd.read_csv(r"D:\games1\ecommerce_data.csv")

# -------------------------------
# NEW SIMPLE HEATMAP (REPLACED)
# -------------------------------
cols = ['time_on_site', 'avg_session_time', 'pages_viewed', 'bounce_rate', 'purchase']

corr = df[cols].corr()

plt.figure(figsize=(6,4))

sns.heatmap(corr,
            annot=True,
            cmap='coolwarm',
            fmt=".2f",
            linewidths=1)

plt.title("Simple Correlation Heatmap")
plt.show()

# -------------------------------
# Purchase Count (SAME AS BEFORE)
# -------------------------------
plt.figure()

sns.countplot(x='purchase', data=df)

plt.title("Total Purchases")
plt.show()