
# Problem 3: Impact of User Engagement on Purchase Behavior
# Ad Click vs Purchase (Bar Chart)
# Returning User vs Purchase (Bar Chart)
# Load dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\games1\ecommerce_data.csv")

plt.figure()
sns.boxplot(y=df['purchase'])
plt.title("Boxplot: Purchase")
plt.show()

Q1 = df['purchase'].quantile(0.25)
Q3 = df['purchase'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_clean = df[(df['purchase'] >= lower) & (df['purchase'] <= upper)]

plt.figure()
df_clean.groupby('ad_clicked')['purchase'].mean().plot(kind='bar')
plt.title("Ad Click vs Purchase (Cleaned)")
plt.show()

plt.figure()
df_clean.groupby('returning_user')['purchase'].mean().plot(kind='bar')
plt.title("Returning User vs Purchase (Cleaned)")
plt.show()