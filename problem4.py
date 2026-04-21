# Linear Relationship (Regression)
# Goal: Session time vs purchase relation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv(r"D:\games1\ecommerce_data.csv")

# Sort values (IMPORTANT for line graph)
df = df.sort_values(by='avg_session_time')

# X and Y
x = df['avg_session_time'].values.reshape(-1,1)
y = df['purchase'].values

# Model
model = LinearRegression()
model.fit(x, y)

# Prediction
y_pred = model.predict(x)

# Plot
plt.figure(figsize=(6,4))

# Line graph (prediction)
plt.plot(df['avg_session_time'], y_pred)

plt.title("Linear Regression (Line Graph): Session Time vs Purchase")
plt.xlabel("Session Time")
plt.ylabel("Predicted Purchase")

plt.show()