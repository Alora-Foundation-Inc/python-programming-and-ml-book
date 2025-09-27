import pandas as pd
import numpy as np

# Fruit data: [size(1-5), sweetness(1-5), is_red, is_green, is_yellow]
fruit_data = [
    {"features": [3, 5, 1, 0, 0], "name": "Apple"},
    {"features": [4, 3, 0, 0, 1], "name": "Banana"},
    {"features": [2, 4, 0, 1, 0], "name": "Lime"},
    {"features": [3, 5, 0, 1, 0], "name": "Green Apple"}
]
fruit_df = pd.DataFrame(fruit_data)
print("Known Fruit Data:")
for _, row in fruit_df.iterrows():
    print(f"Name: {row['name']}, Features: {row['features']}")

# TODOs:
# 1) Define a distance function between two feature vectors (Euclidean).
# 2) For a new fruit (list of 5 numbers), compute its distance to each known fruit.
# 3) Predict the closest fruit (smallest distance). Try a few test vectors!
