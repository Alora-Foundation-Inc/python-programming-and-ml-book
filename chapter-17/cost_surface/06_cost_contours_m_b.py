# Visualize MSE over (m,b) grid and a sample GD path
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8], dtype=float)
y = np.array([3,5,6,7,11,10,13,15], dtype=float)

def mse(m, b):
    return np.mean((m*x + b - y)**2)

m_vals = np.linspace(-1, 3, 80)
b_vals = np.linspace(-4, 6, 80)
Z = np.zeros((len(b_vals), len(m_vals)))
for i, b in enumerate(b_vals):
    for j, m in enumerate(m_vals):
        Z[i,j] = mse(m,b)

# a short GD path
m, b = 0.0, 0.0
lr = 0.01
path = [(m,b)]
for _ in range(80):
    yhat = m*x + b
    dm = (2/len(x)) * np.sum((yhat - y) * x)
    db = (2/len(x)) * np.sum(yhat - y)
    m -= lr*dm
    b -= lr*db
    path.append((m,b))

plt.figure(figsize=(8,6))
CS = plt.contour(m_vals, b_vals, Z, levels=20)
plt.clabel(CS, inline=1, fontsize=8)
plt.plot([p[0] for p in path], [p[1] for p in path], marker="o")
plt.title("MSE Cost Surface over (m,b) with GD path")
plt.xlabel("m (slope)"); plt.ylabel("b (intercept)")
plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
