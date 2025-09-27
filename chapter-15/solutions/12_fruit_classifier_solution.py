import pandas as pd
import numpy as np

fruit_data = [
    {"features": [3, 5, 1, 0, 0], "name": "Apple"},
    {"features": [4, 3, 0, 0, 1], "name": "Banana"},
    {"features": [2, 4, 0, 1, 0], "name": "Lime"},
    {"features": [3, 5, 0, 1, 0], "name": "Green Apple"}
]
df = pd.DataFrame(fruit_data)

def euclid(a, b):
    a = np.array(a, dtype=float); b = np.array(b, dtype=float)
    return np.linalg.norm(a-b)

def classify(x):
    distances = [(row["name"], euclid(x, row["features"])) for _, row in df.iterrows()]
    distances.sort(key=lambda t: t[1])
    return distances[0]

tests = [
    [3,5,1,0,0],   # Apple
    [4,3,0,0,1],   # Banana
    [2,3,0,1,0],   # Closer to Lime
]
for t in tests:
    name, d = classify(t)
    print(f"Input {t} → {name} (distance {d:.2f})")
