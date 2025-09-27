# Classify simple 'flowers' by [petal_len, petal_wid] (toy numbers, not real iris).
import numpy as np
import matplotlib.pyplot as plt
from knn_class.knn_classifier import KNNClassifier  # local import

# Toy dataset: 0=daisy, 1=rose, 2=tulip
X = np.array([
    [2.0, 0.6], [1.8, 0.5], [2.2, 0.7],   # daisies
    [3.5, 1.4], [3.7, 1.5], [3.3, 1.3],   # roses
    [4.5, 1.8], [4.2, 1.6], [4.7, 1.9],   # tulips
], dtype=float)
y = np.array([0,0,0, 1,1,1, 2,2,2], dtype=int)

names = {0:'daisy', 1:'rose', 2:'tulip'}
colors = {0:'tab:green', 1:'tab:red', 2:'tab:orange'}

clf = KNNClassifier(k=3).fit(X, y)
tests = np.array([[2.5,0.8],[3.4,1.4],[4.6,1.7]])
preds = clf.predict(tests)

print("Predictions:", [names[p] for p in preds])

plt.figure(figsize=(6,5))
for label in [0,1,2]:
    pts = X[y==label]
    plt.scatter(pts[:,0], pts[:,1], label=names[label], c=colors[label])
plt.scatter(tests[:,0], tests[:,1], marker='*', s=160, label='tests')
plt.xlabel('petal_len'); plt.ylabel('petal_wid')
plt.title('KNN Flower Classifier (toy)'); plt.grid(True, linestyle=':', alpha=0.6); plt.legend()
plt.show()
