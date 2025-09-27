import numpy as np
import pandas as pd
from utils.knn_classifier import KNNClassifier

df = pd.read_csv('../data/student_habits.csv').dropna()
df = df[df['study_hours'] >= 0]
df = df[df['sleep_hours'].between(0,24)]
df = df[df['social_media_hours'].between(0,24)]

X = df[['study_hours','sleep_hours','social_media_hours']].to_numpy()
y = df['grade'].to_numpy()

clf = KNNClassifier(k=3).fit(X,y)

def advise(plan):
    pred, votes = clf.predict_with_votes([plan])
    pred = pred[0]; votes = votes[0]
    conf = votes.get(pred,0)/sum(votes.values())
    tips = []
    if plan[2] > 3: tips.append('Try less social media.')
    if plan[1] < 8: tips.append('Aim for ~8 hours of sleep.')
    if plan[0] < 5: tips.append('Increase study time.')
    return pred, conf, tips, votes

plans = [[4,7,5],[7,8,2],[3,6,6]]
for p in plans:
    pred, conf, tips, votes = advise(p)
    print(f'Plan={p} -> grade={pred} (confidence={conf:.2f}) votes={votes} tips={tips}')
