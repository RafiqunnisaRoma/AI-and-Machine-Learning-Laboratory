#7.3. K-Means and Feature Scaling

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 1. Load all four Iris features
iris = load_iris()
X = iris.data

# 2. Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Run K-Means on both datasets
for name, data in [("Without Scaling", X),
                   ("With Scaling", X_scaled)]:

    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = model.fit_predict(data)

    print("\n", name)
    print("Cluster Centers:\n", model.cluster_centers_)
    print("Inertia:", round(model.inertia_, 3))
    print("Silhouette Score:", round(silhouette_score(data, labels), 3))

    # 4. Visualize the first two features
    plt.figure()
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap="viridis")
    plt.scatter(model.cluster_centers_[:, 0],
                model.cluster_centers_[:, 1],
                color="red", marker="X", s=200, label="Centers")
    plt.xlabel("Feature 1 (Sepal Length)")
    plt.ylabel("Feature 2 (Sepal Width)")
    plt.title(name)
    plt.legend()
    plt.grid(True)
    plt.show()



