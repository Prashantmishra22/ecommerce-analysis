# Session Time Distribution
# Session Behavior Analysis
# Goal: User engagement ka purchase par effect

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\games1\ecommerce_data.csv")

plt.figure()
sns.boxplot(y=df['avg_session_time'])
plt.title("Boxplot: Session Time")
plt.show()

plt.figure()
sns.boxplot(y=df['bounce_rate'])
plt.title("Boxplot: Bounce Rate")
plt.show()

Q1 = df['avg_session_time'].quantile(0.25)
Q3 = df['avg_session_time'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_clean = df[(df['avg_session_time'] >= lower) & (df['avg_session_time'] <= upper)]

Q1_b = df_clean['bounce_rate'].quantile(0.25)
Q3_b = df_clean['bounce_rate'].quantile(0.75)
IQR_b = Q3_b - Q1_b

lower_b = Q1_b - 1.5 * IQR_b
upper_b = Q3_b + 1.5 * IQR_b

df_clean = df_clean[(df_clean['bounce_rate'] >= lower_b) & (df_clean['bounce_rate'] <= upper_b)]

plt.figure()
sns.histplot(df_clean['avg_session_time'], kde=True)
plt.title("Session Time Distribution (Cleaned)")
plt.show()

plt.figure()
sns.histplot(df_clean['bounce_rate'], kde=True)
plt.title("Bounce Rate Distribution (Cleaned)")
plt.show()

plt.figure()
sns.scatterplot(x='avg_session_time', y='purchase', data=df_clean)
plt.title("Session Time vs Purchase (Cleaned)")
plt.show()