# Fit Sales ≈ slope*month + intercept; examine biggest errors (e.g., holiday spike)
import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1,13,dtype=float)
sales  = np.array([120,130,125,140,150,160,170,165,180,175,190,260], dtype=float)  # December spike

m, b = 0.0, 0.0
lr = 0.01
epochs = 1500

# TODO:
# 1) Implement GD to fit m,b.
# 2) Compute residuals per month; print the top-3 largest absolute errors.
# 3) Plot data + fitted line and discuss limitations of linear models with seasonal spikes.
