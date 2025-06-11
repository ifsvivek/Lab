import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("housing.csv")

numerical_features = df.select_dtypes(include=[np.number]).columns
print(numerical_features)

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


for feature in numerical_features:
    sns.histplot(df[[feature]], bins=30, kde=True)
    plt.tight_layout()
    plt.show()

for feature in numerical_features:
    sns.boxplot(x=df[feature])
    plt.tight_layout()
    plt.show()
