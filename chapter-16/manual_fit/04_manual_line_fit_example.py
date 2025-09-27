# Manual fit example (exercise vs happiness): estimate slope/intercept with endpoints
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [3, 4, 6, 6, 8, 9]

# Use first and last for a rough estimate
m = (y[-1] - y[0]) / (x[-1] - x[0])   # (9-3)/(6-1) = 6/5 = 1.2
# Solve for b using y = m x + b with first point
b = y[0] - m*x[0]                     # 3 - 1.2*1 = 1.8
print(f"Manual estimate: y = {m:.2f}x + {b:.2f}")

plt.figure(figsize=(7,5))
plt.scatter(x, y, s=100, label="Data")
xs = list(range(0,8))
ys = [m*t + b for t in xs]
plt.plot(xs, ys, linestyle="--", label=f"Manual fit: y={m:.2f}x+{b:.2f}")
plt.title("Manual Line Fit — Exercise vs Happiness")
plt.xlabel("Hours"); plt.ylabel("Happiness");
plt.grid(True, linestyle=":", alpha=0.6); plt.legend()
plt.show()
