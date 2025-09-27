import numpy as np
import pandas as pd

df = pd.read_csv('../data/movie_ratings.csv')
users = df['user'].to_numpy()
R = df.drop(columns=['user']).to_numpy(dtype=float)
R = np.nan_to_num(R, nan=0.0)

def user_similarity(u, v):
    a, b = R[u], R[v]
    if np.all(a==0) or np.all(b==0):
        return 0.0
    num = float(np.dot(a, b))
    den = float(np.linalg.norm(a) * np.linalg.norm(b))
    return num/den if den>0 else 0.0

def recommend_for(user_index, k=2, topn=3):
    sims = np.array([user_similarity(user_index, j) for j in range(len(users))])
    sims[user_index] = 0.0
    nbrs = sims.argsort()[::-1][:k]
    scores = np.zeros(R.shape[1])
    for nb in nbrs:
        scores += sims[nb] * R[nb]
    # do not recommend already-rated movies
    already = R[user_index] > 0
    scores[already] = -1
    movie_names = df.columns[1:]
    rec_idx = scores.argsort()[::-1][:topn]
    return list(zip(movie_names[rec_idx], scores[rec_idx]))

print('Top picks for', users[0], '->', recommend_for(0, k=2, topn=3))
