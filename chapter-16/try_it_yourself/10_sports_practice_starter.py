import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

basketball = {
    'Hours_Practiced':        [10, 25, 40, 55, 70, 15, 30, 60, 45, 20],
    'Free_Throw_Percentage':  [45, 60, 72, 80, 85, 50, 65, 82, 75, 55]
}
df = pd.DataFrame(basketball)
print("Basketball Practice Data:\n", df)

# TODOs:
# 1) Scatter with nice labels.
# 2) Regression line; print slope (improvement per hour) and intercept (baseline skill).
# 3) Predict performance at 100 hours and plot it.
# 4) Discuss whether a linear model stays accurate for very high hours (diminishing returns).
