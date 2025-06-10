import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

faces_df = pd.read_csv("faces.csv")
x = faces_df.drop("person_id", axis=1).values
y = faces_df["person_id"].values

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

gnb = GaussianNB()
gnb.fit(x_train, y_train)
y_pred = gnb.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(
    f"Accuracy of Naive Bayes Classifier on Olivetti faces dataset: {accuracy*100:.2f}%"
)

n_samples = 10
plt.figure(figsize=(20, 4))

for i in range(n_samples):
    plt.subplot(2, n_samples, i + 1)
    plt.imshow(x_test[i].reshape(64, 64), cmap="gray")
    plt.title(f"Predicted: {y_pred[i]}\nTrue: {y_test[i]}")
    plt.axis("off")

plt.tight_layout()
plt.show()
