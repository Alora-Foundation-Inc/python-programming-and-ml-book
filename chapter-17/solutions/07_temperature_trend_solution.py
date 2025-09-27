import numpy as np
import matplotlib.pyplot as plt

days = np.array([ 15,  45,  75, 105, 135, 165, 195, 225, 255, 285, 315], dtype=float)
temps= np.array([ 38,  45,  55,  65,  74,  79,  78,  72,  60,  50,  42], dtype=float)

m, b = 0.1, 50.0
lr = 1e-5
epochs = 1000
n = len(days)

for _ in range(epochs):
    yhat = m*days + b
    dm = (2/n) * np.sum((yhat - temps) * days)
    db = (2/n) * np.sum(yhat - temps)
    m -= lr*dm
    b -= lr*db

print(f"slope ≈ {m:.5f}, intercept ≈ {b:.2f}")
print("Interpretation: Positive slope means warmer temps later in the year (up to mid‑summer), then our simple line averages the cool-down.")

xs = np.linspace(days.min(), days.max(), 100)
ys = m*xs + b
plt.figure(figsize=(8,5))
plt.scatter(days, temps, s=100, label="Data")
plt.plot(xs, ys, linestyle="--", label="GD fit")
plt.title("Temperature vs Day — GD Trend Line")
plt.xlabel("Day of Year"); plt.ylabel("Temperature (°F)"); plt.legend(); plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
