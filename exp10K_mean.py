#K_mean Cluster
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

iris = load_iris()

# Use all four features for clustering
X = iris.data

model = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = model.fit_predict(X)

print("Cluster Centers (4 features):\n", model.cluster_centers_)
print("Inertia:", model.inertia_)
print("Silhouette:", silhouette_score(X, labels))

# Visualize only the first two features
plt.scatter(iris.data[:, 0], iris.data[:, 1],
            c=labels, cmap="viridis")

# Show centroid positions in the same two-dimensional projection
plt.scatter(model.cluster_centers_[:, 0],
            model.cluster_centers_[:, 1],
            marker="X", s=200, color="red", label="Centroids")

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("K-means Using All Four Features")
plt.legend()
plt.show()

# task1
for k in [2, 3, 4, 5]:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X)

    print("k =", k)
    print("Inertia:", round(model.inertia_, 3))
    print("Silhouette:", round(silhouette_score(X, labels), 3))
    print()

#task2
# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

for data, name in [(X, "Original"), (X_scaled, "Standardized")]:
    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = model.fit_predict(data)

    print(name, "Features")
    print("Inertia:", round(model.inertia_, 3))
    print("Silhouette:", round(silhouette_score(data, labels), 3))
    print()
