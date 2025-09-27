import numpy as np

# Features: [height_cm, weight_kg, age_years]
alice = np.array([150, 50, 12], dtype=float)
bob   = np.array([160, 60, 13], dtype=float)

d = np.linalg.norm(alice - bob)
print("Multi‑feature Euclidean distance:", round(float(d), 3))
