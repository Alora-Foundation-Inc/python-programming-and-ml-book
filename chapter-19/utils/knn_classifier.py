import numpy as np

class KNNClassifier:
    """Tiny and readable KNN (for teaching).
    - fit(X, y) stores dataset
    - predict(X_new) returns labels
    - predict_with_votes(X_new) also returns vote counts
    """
    def __init__(self, k=3):
        self.k = int(k)
        self.X = None
        self.y = None

    def fit(self, X, y):
        self.X = np.array(X, dtype=float)
        self.y = np.array(y)
        return self

    def _predict_one(self, x):
        d = np.linalg.norm(self.X - x, axis=1)
        idx = np.argsort(d)[:self.k]
        votes = self.y[idx]
        values, counts = np.unique(votes, return_counts=True)
        return values[np.argmax(counts)], dict(zip(values.tolist(), counts.tolist()))

    def predict(self, X):
        X = np.array(X, dtype=float)
        labels = []
        for x in X:
            lab, _ = self._predict_one(x)
            labels.append(lab)
        return np.array(labels)

    def predict_with_votes(self, X):
        X = np.array(X, dtype=float)
        labels, details = [], []
        for x in X:
            lab, votes = self._predict_one(x)
            labels.append(lab)
            details.append(votes)
        return np.array(labels), details
