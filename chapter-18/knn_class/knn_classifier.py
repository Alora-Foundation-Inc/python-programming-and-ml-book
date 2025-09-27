import numpy as np

class KNNClassifier:
    def __init__(self, k=3):
        self.k = int(k)
        self.X = None
        self.y = None

    def fit(self, X, y):
        self.X = np.array(X, dtype=float)
        self.y = np.array(y, dtype=int)
        return self

    def _predict_one(self, x):
        d = np.linalg.norm(self.X - x, axis=1)
        idx = np.argsort(d)[:self.k]
        votes = self.y[idx]
        # majority vote; tie-break: smallest label wins
        values, counts = np.unique(votes, return_counts=True)
        return int(values[np.argmax(counts)])

    def predict(self, X):
        X = np.array(X, dtype=float)
        return np.array([self._predict_one(x) for x in X], dtype=int)
