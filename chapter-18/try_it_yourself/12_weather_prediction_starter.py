# Classify weather type by [temp_F, humidity_%] -> label 0='cool/dry', 1='warm/humid' (toy)
import numpy as np

X = np.array([
    [55, 30], [58, 40], [60, 35], [54, 25],   # cool/dry
    [80, 70], [85, 75], [78, 82], [90, 90],   # warm/humid
], dtype=float)
y = np.array([0,0,0,0, 1,1,1,1], dtype=int)

# TODOs:
# 1) Build/fit a KNNClassifier.
# 2) Predict classes for [[57, 32], [84, 78], [72, 55]].
# 3) Try k=1,3,5 — do results change?
