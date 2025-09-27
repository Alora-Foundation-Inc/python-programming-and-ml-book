import numpy as np
from knn_class.knn_classifier import KNNClassifier

X = np.array([
    [2,8,5],[3,7,6],[1,6,7],[4,8,3],
    [6,8,2],[7,8,1],[5,7,2],[6,9,2]
], dtype=float)
y = np.array([0,0,0,0, 1,1,1,1], dtype=int)

clf = KNNClassifier(k=3).fit(X,y)
tests = np.array([[4,8,3], [7,8,2], [3,6,6]], dtype=float)
preds = clf.predict(tests)
print("Predictions (0=needs support,1=on track):", preds.tolist())
print("k=3 means we look at the 3 closest examples and let them vote on the label.")
