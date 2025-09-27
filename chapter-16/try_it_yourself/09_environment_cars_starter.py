import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

car_efficiency = {
    'Car_Age_Years':     [1, 3, 5, 7, 10, 2, 8, 12, 6, 4],
    'Miles_Per_Gallon':  [35, 32, 28, 25, 20, 34, 23, 18, 27, 30]
}
df = pd.DataFrame(car_efficiency)
print("Car Age vs. Fuel Efficiency:\n", df)

# TODOs:
# 1) Scatter: age vs MPG.
# 2) Fit regression line; print slope (expect negative).
# 3) Predict MPG for a 15‑year‑old car and plot it.
# 4) Explain environmental implications briefly in a print() statement.
