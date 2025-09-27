# Animal game: classify by [legs, speed_score, is_water(0/1)].
# Labels: 0=land animal, 1=water animal
import numpy as np

X = np.array([
    [4, 6, 0], [4, 8, 0], [2, 10, 0],  # land (cheetah-like, etc.)
    [0, 3, 1], [0, 5, 1], [0, 2, 1],   # water
], dtype=float)
y = np.array([0,0,0, 1,1,1], dtype=int)

# TODOs:
# 1) Fit KNNClassifier(k=3).
# 2) Predict for [[4,7,0], [0,4,1], [2,4,0]].
# 3) Print results and add a sentence on why features matter.
