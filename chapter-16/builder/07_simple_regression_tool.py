# Tiny OLS regression calculator (no SciPy). Enter x and y lists; see slope/intercept and plot.
import numpy as np
import matplotlib.pyplot as plt

# Example data (edit these two lists, then run)
x = np.array([1,2,3,4,5], dtype=float)
y = np.array([3,5,7,9,11], dtype=float)

xm, ym = x.mean(), y.mean()
m = ((x - xm) * (y - ym)).sum() / ((x - xm)**2).sum()
b = ym - m*xm

print(f"Best‑fit line (OLS): y = {m:.3f}x + {b:.3f}")

xs = np.linspace(x.min(), x.max(), 100)
ys = m*xs + b

plt.figure(figsize=(7,5))
plt.scatter(x, y, s=100, label="Data")
plt.plot(xs, ys, linestyle="--", label="Best‑fit: y=mx+b")
plt.title("Simple Regression Calculator (from scratch)")
plt.xlabel("x"); plt.ylabel("y") 
plt.grid(True, linestyle=":", alpha=0.6); plt.legend()
plt.show()
