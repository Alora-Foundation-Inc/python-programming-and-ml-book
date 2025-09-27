# Toy medical screening: classify 'risk' by [age, systolic_bp].
import numpy as np
from knn_class.knn_classifier import KNNClassifier

X = np.array([
    [12, 95], [14, 100], [15, 105], [16, 108],   # low risk (0)
    [35, 125], [42, 135], [50, 140],             # medium risk (1)
    [60, 160], [68, 170], [72, 175],             # high risk (2)
], dtype=float)
y = np.array([0,0,0,0, 1,1,1, 2,2,2], dtype=int)

clf = KNNClassifier(k=3).fit(X,y)
tests = np.array([[13, 102], [45, 130], [70, 168]], dtype=float)
preds = clf.predict(tests)
print("Risk classes (0=low,1=med,2=high):", preds.tolist())
