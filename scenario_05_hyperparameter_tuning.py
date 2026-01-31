"""
Scenario 5: Hyperparameter Tuning
Task: Use GridSearchCV to find the best max_depth (values: [3, 5, 7]) and 
n_estimators (values: [50, 100]) for a Random Forest classifier.
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# Example input data
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
model = RandomForestClassifier(random_state=42)

# Define parameter grid
param_grid = {
    'max_depth': [3, 5, 7],
    'n_estimators': [50, 100]
}

# Perform GridSearchCV
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Get best parameters
best_params = grid_search.best_params_
best_score = grid_search.best_score_

# Output
print("Best Parameters:")
print(best_params)
print(f"\nBest Cross-Validation Score: {best_score:.4f}")

# Test on test set
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)
print(f"Test Set Accuracy: {test_accuracy:.4f}")
