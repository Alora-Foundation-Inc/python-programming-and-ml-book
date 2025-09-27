import numpy as np
import pandas as pd
from utils.knn_classifier import KNNClassifier

# Load (has a couple of messy values to clean)
df = pd.read_csv('../data/student_habits.csv')

# Clean
df = df.dropna()
df = df[df['study_hours'] >= 0]
df = df[df['sleep_hours'].between(0, 24)]
df = df[df['social_media_hours'].between(0, 24)]

# Features & label
X = df[['study_hours','sleep_hours','social_media_hours']].to_numpy()
y = df['grade'].to_numpy()

# Train
model = KNNClassifier(k=3).fit(X, y)

# Predict a few
new_students = np.array([[7,8,2], [3,6,6]], dtype=float)
preds, votes = model.predict_with_votes(new_students)

# Quick evaluation (resubstitution baseline)
train_preds = model.predict(X)
acc = (train_preds == y).mean()

print('Predictions:', preds.tolist())
print('Votes:', votes)
print('Training accuracy (baseline):', round(float(acc), 2))
