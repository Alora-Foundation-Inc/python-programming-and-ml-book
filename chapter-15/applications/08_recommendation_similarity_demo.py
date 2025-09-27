import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ratings = {
    "You":      {"Action":5,"Comedy":2,"Drama":4,"Horror":1},
    "Friend A": {"Action":5,"Comedy":1,"Drama":5,"Horror":2},
    "Friend B": {"Action":2,"Comedy":5,"Drama":3,"Horror":1},
    "Friend C": {"Action":4,"Comedy":3,"Drama":4,"Horror":1},
}
df = pd.DataFrame(ratings).T.fillna(0)
print("Ratings:\n", df)

target = df.loc["You"].values

def similarity(a, b):
    # smaller distance -> more similar
    return np.abs(a - b).sum()

scores = {user: similarity(target, row.values) for user,row in df.drop(index="You").iterrows()}
print("Lower is more similar:", scores)
best_friend = min(scores, key=scores.get)
print("Most similar:", best_friend)

# Visual compare
plt.figure(figsize=(7,5))
w = 0.35
x = range(len(df.columns))
plt.bar([i-w/2 for i in x], df.loc["You"], width=w, label="You")
plt.bar([i+w/2 for i in x], df.loc[best_friend], width=w, label=best_friend)
plt.title("Recommendation: Compare Tastes")
plt.xticks(list(x), df.columns); plt.ylabel("Rating (1-5)"); plt.legend(); plt.grid(axis="y", linestyle=":")
plt.show()
