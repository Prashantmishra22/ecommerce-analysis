# Linear Relationship (Regression)
# Goal: Session time vs purchase relation

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\games1\ecommerce_data.csv")
# Create bins
df['session_group'] = pd.cut(df['avg_session_time'], bins=5)

plt.figure(figsize=(6,4))

sns.barplot(x='session_group', y='purchase', data=df)

plt.title("Purchase Rate by Session Time Group")
plt.xticks(rotation=45)
plt.show()