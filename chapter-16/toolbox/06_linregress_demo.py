# Best-fit with SciPy linregress — falls back to numpy.polyfit if SciPy is missing.
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,5,6,7,8], dtype=float)
y = np.array([3,5,6,7,11,10,13,15], dtype=float)

try:
    from scipy.stats import linregress
    res = linregress(x, y)
    m, b, r = res.slope, res.intercept, res.rvalue
    method = "scipy.stats.linregress"
except Exception:
    m, b = np.polyfit(x, y, 1)
    # crude r from correlation
    r = np.corrcoef(x, y)[0,1]
    method = "numpy.polyfit (fallback)"

print(f"Method: {method}\nLine: y = {m:.3f}x + {b:.3f}  (r={r:.3f})")

xs = np.linspace(x.min(), x.max(), 100)
ys = m*xs + b

plt.figure(figsize=(7,5))
plt.scatter(x, y, s=100, label="Data")
plt.plot(xs, ys, linestyle="--", label="Best‑fit line")
plt.title("Best‑Fit Line via linregress / polyfit") 
plt.xlabel("x"); plt.ylabel("y")
plt.grid(True, linestyle=":", alpha=0.6); plt.legend()
plt.show()
