import pandas as pd
import numpy as np

movie_ratings = {
    "You": {"Action": 5, "Comedy": 2, "Drama": 4, "Horror": 1},
    "Friend A": {"Action": 5, "Comedy": 1, "Drama": 5, "Horror": 2},
    "Friend B": {"Action": 2, "Comedy": 5, "Drama": 3, "Horror": 1},
    "Friend C": {"Action": 4, "Comedy": 3, "Drama": 4, "Horror": 1}
}
df = pd.DataFrame(movie_ratings).T.fillna(0)

def dist(a, b): return np.abs(a-b).sum()

you = df.loc["You"].values
scores = {f: dist(you, df.loc[f].values) for f in df.index if f != "You"}
twin = min(scores, key=scores.get)
print("Most similar friend:", twin, "| distance:", scores[twin])

# Recommend a genre your twin rated higher than you
diff = df.loc[twin] - df.loc["You"]
recommend_genre = diff.idxmax()
print("Recommendation:", recommend_genre)
