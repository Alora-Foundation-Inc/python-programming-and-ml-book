import numpy as np
import matplotlib.pyplot as plt

# Simple 2-class toy set
red  = np.array([[1,1],[2,1],[2,2],[3,2]], dtype=float)
blue = np.array([[4,4],[5,4],[5,5],[6,5]], dtype=float)
X = np.vstack([red, blue])
y = np.array([0]*len(red) + [1]*len(blue))  # 0=red, 1=blue

def knn_predict(x, k):
    d = np.linalg.norm(X - x, axis=1)
    idx = np.argsort(d)[:k]
    votes = y[idx]
    # majority vote (ties -> lower label)
    values, counts = np.unique(votes, return_counts=True)
    return int(values[np.argmax(counts)])

test = np.array([[3.2, 2.6],[4.2, 3.3]])
for k in [1,3,5]:
    preds = [knn_predict(t, k) for t in test]
    print(f"k={k}: predictions ->", preds)

# plot
plt.figure(figsize=(6,5))
plt.scatter(red[:,0], red[:,1], label='Red (0)')
plt.scatter(blue[:,0], blue[:,1], label='Blue (1)')
plt.scatter(test[:,0], test[:,1], s=120, marker='*', label='Tests')
plt.title('Comparing different k values'); plt.legend(); plt.grid(True, linestyle=':', alpha=0.6)
plt.show()
