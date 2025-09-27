import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Basketball player: distance vs shooting percentage
player_data = {
    'Distance_Feet': [5, 8, 12, 15, 18, 20, 25, 30],
    'Shooting_Percentage': [85, 78, 65, 58, 45, 40, 30, 25]
}
df_player = pd.DataFrame(player_data)

# TODO:
# 1) Scatter plot distance vs shooting%.
# 2) Fit a best-fit line with linregress; plot it.
# 3) Print the equation; explain what the slope means.
# 4) Predict shooting% at 10 feet and 22 feet; plot those predictions.
# 5) (Advanced) Compare a second player with a different dataset.
