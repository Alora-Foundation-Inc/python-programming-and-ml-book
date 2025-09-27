# Toy fraud detection: [amount, time_of_day(0-23)] → label 0=normal, 1=suspicious
import numpy as np
from knn_class.knn_classifier import KNNClassifier

X = np.array([
    [20, 14], [35, 16], [25, 12], [40, 15],   # normal
    [300, 2], [260, 1], [280, 3],             # large late-night = suspicious
], dtype=float)
y = np.array([0,0,0,0, 1,1,1], dtype=int)

clf = KNNClassifier(k=3).fit(X,y)
tests = np.array([[30,13],[270,2]], dtype=float)
preds = clf.predict(tests)
print("Fraud predictions (0=ok,1=suspicious):", preds.tolist())
