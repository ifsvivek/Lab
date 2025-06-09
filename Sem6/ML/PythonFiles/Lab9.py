import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Load data
df = pd.read_csv('faces.csv')
X = df.drop('person_id', axis=1)
y = df['person_id']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Naive Bayes
nb = GaussianNB()
nb.fit(X_train, y_train)

# Predict and evaluate
y_pred = nb.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.3f}")
print(f"Number of people: {len(set(y))}")
print(f"Test samples: {len(X_test)}")

# Show sample face image
try:
    img_size = int(np.sqrt(X.shape[1]))
    sample_img = np.array(X.iloc[0]).reshape(img_size, img_size)
    
    plt.figure(figsize=(6, 6))
    plt.imshow(sample_img, cmap='gray')
    plt.title('Sample Face Image')
    plt.axis('off')
    plt.show()
except:
    print("Could not display sample image")
