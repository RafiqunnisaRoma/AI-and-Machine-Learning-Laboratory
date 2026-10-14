#5 . Decision tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report

# 1. Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# 2. Split data into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, stratify=y, random_state=42
)

# 3. Train trees with different depths
depths = [1, 2, 3, 4, None]
results = []

for depth in depths:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_acc = accuracy_score(y_train, train_pred)
    test_acc = accuracy_score(y_test, test_pred)

    results.append((depth, train_acc, test_acc, model))

    print("Depth:", depth)
    print("Training Accuracy:", round(train_acc, 3))
    print("Testing Accuracy:", round(test_acc, 3))
    print()

# 4. Select the model with the highest test accuracy
best = max(results, key=lambda item: item[2])
best_depth, train_acc, test_acc, best_model = best

print("Best Depth:", best_depth)
print("Best Test Accuracy:", round(test_acc, 3))

# 5. Confusion matrix
y_pred = best_model.predict(X_test)
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 6. Precision, Recall and F1-score
print("\nClassification Report:")
print(classification_report(y_test, y_pred,
                            target_names=iris.target_names))