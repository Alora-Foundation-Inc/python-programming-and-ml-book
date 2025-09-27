# Toy recommendation: users rated genres [Action, Comedy, Drama]; classify new user to a 'taste group'.
import numpy as np
from knn_class.knn_classifier import KNNClassifier

# 0 = Action-lover, 1 = Comedy-lover, 2 = Drama-lover
X = np.array([
    [5,1,2], [4,2,2], [5,1,1],      # action
    [1,5,2], [2,4,2], [1,5,3],      # comedy
    [2,2,5], [1,3,5], [2,1,5],      # drama
], dtype=float)
y = np.array([0,0,0, 1,1,1, 2,2,2], dtype=int)

clf = KNNClassifier(k=3).fit(X,y)
tests = np.array([[4,2,2], [2,4,3], [1,2,5]], dtype=float)
preds = clf.predict(tests)
print("Taste group predictions:", preds.tolist())
