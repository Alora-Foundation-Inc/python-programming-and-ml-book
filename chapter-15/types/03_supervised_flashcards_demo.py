import numpy as np
import matplotlib.pyplot as plt

# "Flashcards": hours (x) with known scores (y) → learn line y = m x + b
x = np.array([1,2,3,4,5,6], dtype=float)
y = np.array([50,60,70,80,90,100], dtype=float)

# Fit with a simple best-fit line (polyfit degree 1)
m, b = np.polyfit(x, y, 1)
print(f"Learned line (supervised): y = {m:.2f}*x + {b:.2f}")

# Predict new
x_new = np.array([7,8])
y_pred = m*x_new + b
print("Predictions:", dict(zip(x_new, y_pred)))

plt.figure(figsize=(7,5))
plt.scatter(x, y, s=100, label="Labeled data")
xs = np.linspace(1,8,50)
plt.plot(xs, m*xs + b, linestyle="--", label="Learned line")
plt.scatter(x_new, y_pred, label="Predictions")
plt.title("Supervised Learning: Learn from Labeled Examples")
plt.xlabel("Hours"); plt.ylabel("Score"); plt.grid(True, linestyle=":"); plt.legend()
plt.show()
