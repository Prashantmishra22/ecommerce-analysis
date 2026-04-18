# Session Time Distribution
# Session Behavior Analysis
# Goal: User engagement ka purchase par effect

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\games1\ecommerce_data.csv")

plt.figure()
sns.histplot(df['avg_session_time'], kde=True)
plt.title("Session Time Distribution")
plt.show()

# Bounce Rate Distribution
plt.figure()
sns.histplot(df['bounce_rate'], kde=True)
plt.title("Bounce Rate Distribution")
plt.show()

# Session Time vs Purchase
plt.figure()
sns.scatterplot(x='avg_session_time', y='purchase', data=df)
plt.title("Session Time vs Purchase")
plt.show()