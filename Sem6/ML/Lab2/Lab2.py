"""Converted from Lab2.ipynb"""

# Import the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../Lab1/housing.csv")


# Display the first few rows of the dataset
print("Dataset Overview:")
print(f"Number of samples: {df.shape[0]}")
print(f"Number of features: {df.shape[1]}")
print("\nFeature descriptions:")
for column in df.columns:
    print(f"- {column}")

df.head()

# Display basic statistics of the dataset
df.describe()

# Compute the correlation matrix
corr_matrix = df.corr(numeric_only=True)

# Display the correlation matrix
print("Correlation Matrix:")
corr_matrix

dp=sns.heatmap(df.corr(numeric_only=True),annot=True)

sns.pairplot(df)