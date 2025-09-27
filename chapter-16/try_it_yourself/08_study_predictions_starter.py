import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import isnan

# Study hours vs test scores (clean linear)
study_scores = {
    'Study_Hours': [1, 2, 3, 4, 5],
    'Test_Score':  [65, 70, 75, 80, 85]
}
df = pd.DataFrame(study_scores)
print("Study Hours vs. Test Scores:\n", df)

# TODOs:
# 1) Compute slope/intercept (use numpy.polyfit or linregress if available).
# 2) Print equation: score = m * hours + b
# 3) Predict scores for 3.5 hours and 7 hours; add both to the plot.
# 4) Discuss: Is 7 hours an extrapolation? Why might that be less reliable?
