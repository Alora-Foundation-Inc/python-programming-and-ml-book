import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1,13,dtype=float)
sales  = np.array([120,130,125,140,150,160,170,165,180,175,190,260], dtype=float)

m, b = 0.0, 0.0
lr = 0.01
epochs = 2000
n = len(months)

for _ in range(epochs):
    yhat = m*months + b
    dm = (2/n) * np.sum((yhat - sales) * months)
    db = (2/n) * np.sum(yhat - sales)
    m -= lr*dm
    b -= lr*db

print(f"Line: sales ≈ {m:.2f}*month + {b:.2f}")

residuals = sales - (m*months + b)
idx = np.argsort(-np.abs(residuals))[:3]
print("Top-3 absolute errors:")
for i in idx:
    print(f"  Month {int(months[i])}: actual={sales[i]}, pred={(m*months[i]+b):.1f}, error={residuals[i]:+.1f}")

xs = np.linspace(1,12,100)
ys = m*xs + b
plt.figure(figsize=(8,5))
plt.scatter(months, sales, s=100, label="Data")
plt.plot(xs, ys, linestyle="--", label="GD fit")
plt.title("Sales Forecasting — Linear Fit with Outlier/Seasonal Spike")
plt.xlabel("Month"); plt.ylabel("Sales"); plt.legend(); plt.grid(True, linestyle=":", alpha=0.6)
plt.show()

print("Takeaway: Linear trend gives a baseline, but seasonal spikes (e.g., December) break the straight-line assumption.")
