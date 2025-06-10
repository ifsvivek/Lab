import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

values = np.random.rand(100)
labels = ["Class1" if x <= 0.5 else "Class2" for x in values[:50]] + [None] * 50

df = pd.DataFrame({"Point": [f"x{i+1}" for i in range(100)], "Value": values, "Label": labels})
labeled, unlabeled = df[df["Label"].notna()], df[df["Label"].isna()]

X_train, y_train = labeled[["Value"]], labeled["Label"]
X_test = unlabeled[["Value"]]
true_labels = ["Class1" if x <= 0.5 else "Class2" for x in values[50:]]

for k in [1, 2, 3, 4, 5, 20, 30]:
    predictions = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train).predict(X_test)
    accuracy = accuracy_score(true_labels, predictions) * 100
    print(f"Accuracy for k={k}: {accuracy:.2f}%")
