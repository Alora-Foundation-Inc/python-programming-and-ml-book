import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

# Make three rough "hobby groups" without labels (just 2D points)
group1 = np.random.normal(loc=[2,8],  scale=0.6, size=(20,2))
group2 = np.random.normal(loc=[6,6],  scale=0.6, size=(20,2))
group3 = np.random.normal(loc=[8,2],  scale=0.6, size=(20,2))
X = np.vstack([group1, group2, group3])

# K-means from scratch (k=3), very small & readable
k = 3
centers = X[np.random.choice(len(X), k, replace=False)]

def assign(X, centers):
    # returns cluster index for each point
    dists = np.sqrt(((X[:,None,:] - centers[None,:,:])**2).sum(axis=2))
    return dists.argmin(axis=1)

def update(X, labels, k):
    return np.array([X[labels==i].mean(axis=0) for i in range(k)])

for _ in range(8):
    labels = assign(X, centers)
    new_centers = update(X, labels, k)
    if np.allclose(new_centers, centers): break
    centers = new_centers

print("Cluster centers:\n", centers)

# Plot clusters
colors = np.array(["tab:blue","tab:orange","tab:green"])
plt.figure(figsize=(6,6))
for i in range(k):
    pts = X[labels==i]
    plt.scatter(pts[:,0], pts[:,1], s=40, label=f"Cluster {i+1}")
plt.scatter(centers[:,0], centers[:,1], s=200, marker="X", label="Centers")
plt.title("Unsupervised: K-means Discovers Groups (No Labels Given)")
plt.xlabel("Feature 1"); plt.ylabel("Feature 2"); plt.legend(); plt.grid(True, linestyle=":")
plt.show()
