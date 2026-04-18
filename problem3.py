import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_csv(r"D:\games1\ecommerce_data.csv")

sns.set(style="whitegrid")

# -------------------------
# Graph 1: Ad Click vs Purchase
# -------------------------
plt.figure(figsize=(6,4))
sns.barplot(x='ad_clicked', y='purchase', data=df)

plt.title("Ad Click vs Purchase Rate")
plt.xlabel("Ad Clicked (0 = No, 1 = Yes)")
plt.ylabel("Purchase Rate")

plt.tight_layout()
plt.show()


# -------------------------
# Graph 2: Returning User vs Purchase
# -------------------------
plt.figure(figsize=(6,4))
sns.barplot(x='returning_user', y='purchase', data=df)

plt.title("Returning User vs Purchase Rate")
plt.xlabel("Returning User (0 = No, 1 = Yes)")
plt.ylabel("Purchase Rate")

plt.tight_layout()
plt.show()


# -------------------------
# Graph 3: Purchase Distribution (Pie Chart)
# -------------------------
plt.figure(figsize=(5,5))

df['purchase'].value_counts().plot.pie(
    autopct='%1.1f%%',
    labels=["No Purchase", "Purchase"]
)

plt.title("Overall Purchase Distribution")
plt.ylabel("")

plt.show()