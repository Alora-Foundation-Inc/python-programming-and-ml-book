import numpy as np
from knn_class.knn_classifier import KNNClassifier

X = np.array([
    [55,30],[58,40],[60,35],[54,25],
    [80,70],[85,75],[78,82],[90,90]
], dtype=float)
y = np.array([0,0,0,0, 1,1,1,1], dtype=int)

for k in [1,3,5]:
    clf = KNNClassifier(k=k).fit(X,y)
    tests = np.array([[57,32],[84,78],[72,55]], dtype=float)
    preds = clf.predict(tests)
    print(f"k={k} ->", preds.tolist())
print("Larger k smooths decisions but can blur sharp boundaries.")
