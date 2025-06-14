"""Converted from Lab2.ipynb"""

import pandas as pd

df= pd.read_csv('data.csv')
print(df)

print(df.marks[0])


print(df.marks[0:2])
print(df[1:3])

print(df[["id", "marks"]])

print(df.iloc[0:2, 1:3])

print(df.loc[0:2, ["id", "marks"]])

print(f"Mean of marks: {df['marks'].mean()}")
print(f"Sum of marks: {df['marks'].sum()}")
print(f"Standard deviation of marks: {df['marks'].std()}")
print(f"Variance of marks: {df['marks'].var()}")

print(f"Median of marks: {df['marks'].median()}")
print(f"Mode of marks: {df['marks'].mode()[0]}")
print(f"Max of marks: {df['marks'].max()}")
print(f"Min of marks: {df['marks'].min()}")
print(f"Count of marks: {df['marks'].count()}")

print(df.head())
print(df.shape)
print(df.describe())

print(df.isnull())
print(df.notnull())

print(df.tail())

import numpy as np

numerical_features = df.select_dtypes(include=[np.number]).columns
print(numerical_features)

# Import visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns


x=[1, 2, 3, 4, 5]
y=[10, 20, 25, 30, 35]
plt.plot(x, y, marker='o')
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()