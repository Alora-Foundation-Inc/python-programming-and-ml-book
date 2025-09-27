import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

months = np.array([1, 2, 3, 4, 5, 6])
A = np.array([15000, 16500, 18000, 19200, 20800, 22500])
B = np.array([25000, 24800, 24200, 23500, 22900, 22000])

df = pd.DataFrame({"Month": months, "A": A, "B": B})
print(df)

# Fit lines
mA, bA, *_ = linregress(months, A)
mB, bB, *_ = linregress(months, B)
print(f"A: y = {mA:.2f}x + {bA:.0f}")
print(f"B: y = {mB:.2f}x + {bB:.0f}")

# Predict month 12
x_pred = 12
pred_A = mA*x_pred + bA
pred_B = mB*x_pred + bB

plt.figure(figsize=(9,5))
plt.plot(df["Month"], df["A"], marker="o", label="Business A")
plt.plot(df["Month"], df["B"], marker="o", label="Business B")

xs = np.arange(1, 13)
plt.plot(xs, mA*xs+bA, linestyle="--", label="A trend")
plt.plot(xs, mB*xs+bB, linestyle="--", label="B trend")

plt.scatter([x_pred],[pred_A], label=f"A @12 ≈ {pred_A:.0f}")
plt.scatter([x_pred],[pred_B], label=f"B @12 ≈ {pred_B:.0f}")

# Rough overtake month (solve mA*x+bA = mB*x+bB)
if mA != mB:
    x_cross = (bB - bA) / (mA - mB)
    if 0 < x_cross <= 24:
        plt.axvline(x_cross, linestyle=":", alpha=0.6)
        plt.text(x_cross+0.1, min(A.min(),B.min()), f"Cross ≈ {x_cross:.1f}", rotation=90)

plt.title("Business Growth Analyzer")
plt.xlabel("Month"); plt.ylabel("Revenue ($)"); plt.grid(axis="y", linestyle=":", alpha=0.6)
plt.legend()
plt.show()
