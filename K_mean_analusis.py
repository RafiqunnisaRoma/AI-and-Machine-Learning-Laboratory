#Exp9 K-mean model selection and elbow , sihouette

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load first two Iris features
iris = load_iris()
X = iris.data[:, :2]

inertias = []
sil_score = []
ks = [2, 3, 4, 5]

# Test different values of k
for k in ks:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X)

    inertias.append(model.inertia_)  # Store inertia
    sil_score.append(silhouette_score(X, labels))  # Store silhouette

    print(f"k={k}, Inertia={model.inertia_:.3f}, "
          f"Silhouette={sil_score[-1]:.3f}")

# Elbow graph
plt.plot(ks, inertias, marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.grid(True)
plt.show()

# Silhouette graph
plt.plot(ks, sil_score, marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score vs k")
plt.grid(True)
plt.show()

# Select k with the highest silhouette score
best_k = ks[sil_score.index(max(sil_score))]
print("Selected k =", best_k)

# Fit final model
final_model = KMeans(n_clusters=best_k, random_state=42, n_init=10)
labels = final_model.fit_predict(X)
centers = final_model.cluster_centers_

# Plot final clusters and centers
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis")
plt.scatter(centers[:, 0], centers[:, 1], marker="X",
            s=200, color="red", label="Cluster centers")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title(f"K-Means Clusters (k={best_k})")
plt.legend()
plt.grid(True)
plt.show()


