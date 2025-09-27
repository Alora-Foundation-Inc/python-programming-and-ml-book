import numpy as np
import pandas as pd
from utils.knn_classifier import KNNClassifier

df = pd.read_csv('../data/medical_patients.csv')
features = ['age','systolic_bp','cholesterol','chest_pain']
X = df[features].to_numpy(dtype=float)
y = df['diagnosis'].to_numpy()

# min-max normalize for fair distances
mins = X.min(axis=0)
maxs = X.max(axis=0)
rng = np.where(maxs - mins == 0, 1.0, maxs - mins)
Xn = (X - mins) / rng

clf = KNNClassifier(k=5).fit(Xn, y)

def predict_patient(sample):
    s = np.array(sample, dtype=float)
    sn = (s - mins) / rng
    lab, votes = clf._predict_one(sn)
    total = sum(votes.values())
    conf = votes.get(lab, 0) / max(1, total)
    return lab, conf, votes

tests = [[13,102,150,0],[45,130,215,1],[70,170,275,1]]
for t in tests:
    lab, conf, votes = predict_patient(t)
    print(f"Input={t} -> {lab} (confidence={conf:.2f}; votes={votes})")
