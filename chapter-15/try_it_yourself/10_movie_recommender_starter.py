import pandas as pd
import numpy as np

movie_ratings = {
    "You": {"Action": 5, "Comedy": 2, "Drama": 4, "Horror": 1},
    "Friend A": {"Action": 5, "Comedy": 1, "Drama": 5, "Horror": 2},
    "Friend B": {"Action": 2, "Comedy": 5, "Drama": 3, "Horror": 1},
    "Friend C": {"Action": 4, "Comedy": 3, "Drama": 4, "Horror": 1}
}
df = pd.DataFrame(movie_ratings).T.fillna(0)
print("Movie Ratings Data:\n", df)

# TODOs:
# 1) Pick 'You' as the target.
# 2) Compute similarity between 'You' and each friend (sum of absolute differences).
# 3) Find the most similar friend (lowest total difference).
# 4) Recommend a genre your twin loves that you rated lower — or suggest a specific title you pick for that genre.
