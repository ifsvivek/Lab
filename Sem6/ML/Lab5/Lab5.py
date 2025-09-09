"""Converted from Lab5.ipynb"""

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

values = np.random.rand(100)
labels = []

for i in values[:50]:
    if i <= 0.5:
        labels.append("Class1")
    else:
        labels.append("Class2")

labels += [None] * 50

data = {"Point": [f"x{i+1}" for i in range(100)], "Value": values, "Label": labels}
df = pd.DataFrame(data)

labelled_df = df[df["Label"].notna()]
unlabeled_df = df[df["Label"].isna()]

X_train = labelled_df[["Value"]]
y_train = labelled_df["Label"]

X_test = unlabeled_df[["Value"]]

k_values = [1, 2, 3, 4, 5, 20, 30]

results = {}
accuracies = {}

true_labels = ["Class1" if x <= 0.5 else "Class2" for x in values[50:]]

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    results[k] = predictions
    accuracy = accuracy_score(true_labels, predictions) * 100
    accuracies[k] = accuracy
    print(f"Accuracy for k={k}: {accuracy:.2f}%")
    unlabeled_df[f"Label_k{k}"] = predictions