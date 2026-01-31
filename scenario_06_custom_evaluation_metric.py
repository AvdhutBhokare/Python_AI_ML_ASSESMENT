"""
Scenario 6: Custom Evaluation Metric
Task: Implement a custom metric weighted_accuracy where class 0 has a weight of 1 
and class 1 has a weight of 2.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Custom metric function
def weighted_accuracy(y_true, y_pred):
    weights = {0: 1, 1: 2}
    
    correct = 0
    total_weight = 0
    
    for true_label, pred_label in zip(y_true, y_pred):
        weight = weights[true_label]
        total_weight += weight
        if true_label == pred_label:
            correct += weight
    
    return correct / total_weight


# Example input data
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate weighted accuracy
score = weighted_accuracy(y_test, y_pred)

# Output
print(f"Weighted Accuracy: {score:.4f}")
print(f"\nClass distribution in test set:")
print(f"Class 0: {np.sum(y_test == 0)} samples (weight: 1)")
print(f"Class 1: {np.sum(y_test == 1)} samples (weight: 2)")
