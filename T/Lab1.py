"""
Lab1: Data Exploration and Visualization
Housing Dataset Analysis
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("housing.csv")


# Select numerical features
numerical_features = df.select_dtypes(include=[np.number]).columns
print(numerical_features)


# Outlier detection using IQR method
for feature in numerical_features:
    q1 = np.percentile(df[feature].dropna(), 25)
    q3 = np.percentile(df[feature].dropna(), 75)
    IQR = q3 - q1
    lower_bound = q1 - 1.5 * IQR
    upper_bound = q3 + 1.5 * IQR
    outliers = df[(df[feature] < lower_bound) | (df[feature] > upper_bound)]
    print(f"\nFeature: {feature}")
    print(f"Q1: {q1}")
    print(f"Q3: {q3}")
    print(f"IQR: {IQR}")
    print(f"Outliers for {feature}:")
    print(f"Number of outliers: {len(outliers)}")

# Combined histogram plots in subplots
plt.figure(figsize=(20, 15))
num_features = len(numerical_features)
rows = (num_features + 2) // 3  # Calculate number of rows needed (3 plots per row)

for i, feature in enumerate(numerical_features):
    plt.subplot(rows, 3, i + 1)
    sns.histplot(df[feature], bins=30, kde=True)
    plt.title(f"Histogram of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# Combined boxplot plots in subplots
plt.figure(figsize=(20, 15))
num_features = len(numerical_features)
rows = (num_features + 2) // 3  # Calculate number of rows needed (3 plots per row)

for i, feature in enumerate(numerical_features):
    plt.subplot(rows, 3, i + 1)
    sns.boxplot(x=df[feature])
    plt.title(f"Boxplot of {feature}")
    plt.xlabel(feature)

plt.tight_layout()
plt.show()
