# Learn y = m x + b with gradient descent (MSE) — tiny, readable
import numpy as np
import matplotlib.pyplot as plt

# toy data (roughly linear)
x = np.array([1,2,3,4,5,6,7,8], dtype=float)
y = np.array([3,5,6,7,11,10,13,15], dtype=float)

m, b = 0.0, 0.0
lr = 0.01
epochs = 2000

n = len(x)
for _ in range(epochs):
    yhat = m*x + b
    # gradients for MSE
    dm = (2/n) * np.sum((yhat - y) * x)
    db = (2/n) * np.sum(yhat - y)
    m -= lr*dm
    b -= lr*db

print(f"Learned line: y ≈ {m:.3f}x + {b:.3f}")

# plot data and final line
xs = np.linspace(x.min(), x.max(), 100)
ys = m*xs + b
plt.figure(figsize=(7,5))
plt.scatter(x, y, s=100, label="Data")
plt.plot(xs, ys, linestyle="--", label="GD fit")
plt.title("Linear Regression via Gradient Descent")
plt.xlabel("x"); plt.ylabel("y"); plt.legend(); plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
