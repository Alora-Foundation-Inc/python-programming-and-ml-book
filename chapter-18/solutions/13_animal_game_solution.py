import numpy as np
from knn_class.knn_classifier import KNNClassifier

X = np.array([
    [4,6,0],[4,8,0],[2,10,0],
    [0,3,1],[0,5,1],[0,2,1]
], dtype=float)
y = np.array([0,0,0, 1,1,1], dtype=int)

clf = KNNClassifier(k=3).fit(X,y)
tests = np.array([[4,7,0],[0,4,1],[2,4,0]], dtype=float)
preds = clf.predict(tests)
print("Predictions (0=land,1=water):", preds.tolist())
print("Why features matter: similar animals have similar numbers, so nearest neighbors tend to share the same label.")
