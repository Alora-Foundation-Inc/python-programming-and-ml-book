import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Monthly revenue data for two businesses
months = np.array([1, 2, 3, 4, 5, 6])
business_a_revenue = np.array([15000, 16500, 18000, 19200, 20800, 22500])
business_b_revenue = np.array([25000, 24800, 24200, 23500, 22900, 22000])

# TODO:
# 1) Build a DataFrame with Month, Business_A_Revenue, Business_B_Revenue.
# 2) Plot both series on one line graph.
# 3) Use linregress to get slope (growth rate) for each. Print it.
# 4) Predict revenue at month 12 using each line. Plot the predictions.
# 5) (Advanced) Estimate when A might pass B by solving mA*x+bA = mB*x+bB.
