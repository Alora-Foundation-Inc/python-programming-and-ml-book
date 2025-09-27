import numpy as np
import pandas as pd

df = pd.read_csv('../data/weather_history.csv')
feat_cols = ['temp_F','humidity','wind_mph']
X = df[feat_cols].to_numpy(dtype=float)
y = df['condition'].to_numpy()

# scale by max for each feature
maxs = X.max(axis=0); maxs[maxs==0] = 1
Xs = X / maxs

def predict(sample, k=3):
    s = np.array(sample, dtype=float)/maxs
    d = np.linalg.norm(Xs - s, axis=1)
    idx = np.argsort(d)[:k]
    nbr_labels = y[idx]
    values, counts = np.unique(nbr_labels, return_counts=True)
    label = values[np.argmax(counts)]
    votes = dict(zip(values.tolist(), counts.tolist()))
    conf = votes[label]/k
    return label, conf, votes

tests = [[82,72,8],[45,40,12],[68,55,9]]
for t in tests:
    lab, conf, votes = predict(t, k=3)
    print(f'{t} -> {lab} (conf={conf:.2f}, votes={votes})')
