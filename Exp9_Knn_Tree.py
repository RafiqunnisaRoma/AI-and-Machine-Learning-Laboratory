#Knn Decision tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

# 1. Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split dataset: 70% training, 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y)

# 3. Create models
k = 5
knn = KNeighborsClassifier(n_neighbors=k)
tree = DecisionTreeClassifier(max_depth=3, random_state=42)

# 4. Train models
knn.fit(X_train, y_train)
tree.fit(X_train, y_train)

# 5. Predict test labels
pred_knn = knn.predict(X_test)
pred_tree = tree.predict(X_test)

# 6. Display results
print("k-NN Accuracy:", accuracy_score(y_test, pred_knn))
print("k-NN Confusion Matrix:\n", confusion_matrix(y_test, pred_knn))

print("\nDecision Tree Accuracy:",
      accuracy_score(y_test, pred_tree))
print("Decision Tree Confusion Matrix:\n",
      confusion_matrix(y_test, pred_tree))

#task 1

for k in [1, 3, 5, 7]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, pred)

    print("k =", k, "| Test Accuracy =", round(accuracy * 100, 2), "%")

#task2
# Standardize using training data only
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train and test k-NN
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Standardized k-NN Accuracy:",
      round(accuracy_score(y_test, pred) * 100, 2), "%")
#task 3

for depth in [1, 2, 3, 5, None]:
    model = DecisionTreeClassifier(
        max_depth=depth, random_state=42
    )
    model.fit(X_train, y_train)

    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))

    print("Depth:", depth,
          "| Train:", round(train_acc * 100, 2), "%",
          "| Test:", round(test_acc * 100, 2), "%")