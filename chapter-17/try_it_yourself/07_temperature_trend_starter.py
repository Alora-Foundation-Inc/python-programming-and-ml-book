# Fit Temperature ≈ slope*day + intercept using gradient descent
import numpy as np
import matplotlib.pyplot as plt

# Example days (large x-values → small learning rate)
days = np.array([ 15,  45,  75, 105, 135, 165, 195, 225, 255, 285, 315], dtype=float)
temps= np.array([ 38,  45,  55,  65,  74,  79,  78,  72,  60,  50,  42], dtype=float)

m, b = 0.1, 50.0
lr = 1e-5
epochs = 1000

# TODO:
# 1) Implement gradient descent for m and b (MSE).
# 2) Plot points + final line; print slope & intercept and interpret the trend.
