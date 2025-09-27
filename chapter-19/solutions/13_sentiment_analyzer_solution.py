import numpy as np
import pandas as pd
from utils.knn_classifier import KNNClassifier

pos_words = {'love','awesome','amazing','great','good','cool'}
neg_words = {'hate','terrible','boring','bad','ugh','disappointed'}

def featurize(text):
    t = text.lower()
    pw = sum(w in t for w in pos_words)
    nw = sum(w in t for w in neg_words)
    ex = t.count('!')
    return [pw, nw, ex]

df = pd.read_csv('../data/sentiment_samples.csv')
X = np.array([featurize(s) for s in df['text'].astype(str).tolist()], dtype=float)
y = df['label'].to_numpy()

clf = KNNClassifier(k=3).fit(X,y)

tests = [
    "I LOVE this!! amazing effects!!!",
    "meh... it was fine",
    "boring plot and terrible acting"
]
for t in tests:
    pred = clf.predict([featurize(t)])[0]
    print(f"{t!r} -> {pred}")
