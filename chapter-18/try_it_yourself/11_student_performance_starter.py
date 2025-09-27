# Classify study plan success from [hours_per_week, sleep_hours, snacks_per_day].
# Labels: 0 = needs support, 1 = on track.
import numpy as np

X = np.array([
    [2, 8, 5], [3, 7, 6], [1, 6, 7], [4, 8, 3],   # needs support (0)
    [6, 8, 2], [7, 8, 1], [5, 7, 2], [6, 9, 2],   # on track (1)
], dtype=float)
y = np.array([0,0,0,0, 1,1,1,1], dtype=int)

# TODOs:
# 1) Import and create KNNClassifier(k=3), fit on X,y.
# 2) Predict for new plans: [[4,8,3], [7,8,2], [3,6,6]].
# 3) Print predictions and explain briefly what 'k' means.
