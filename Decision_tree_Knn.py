#Decision tree vs Knn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report
import numpy as np

# 1. Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# 2. Split data into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

# 3. Train k-NN without scaling
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_knn = knn.predict(X_test)

# 4. Train Decision Tree
tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)
y_tree = tree.predict(X_test)

# 5. Standardize features for k-NN
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn_scaled = KNeighborsClassifier(n_neighbors=5)
knn_scaled.fit(X_train_scaled, y_train)
y_scaled = knn_scaled.predict(X_test_scaled)

# 6. Evaluate all models
models = {
    "k-NN (without scaling)": y_knn,
    "Decision Tree": y_tree,
    "k-NN (with scaling)": y_scaled
}

for name, pred in models.items():
    print("\n", name)
    print("Accuracy:", accuracy_score(y_test, pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
    print(classification_report(
        y_test, pred, target_names=iris.target_names,
        zero_division=0
    ))

    # Identify misclassified test samples
    errors = np.where(y_test != pred)[0]
    print("Misclassified test positions:", errors)
    print("Actual classes:", y_test[errors])
    print("Predicted classes:", pred[errors])
