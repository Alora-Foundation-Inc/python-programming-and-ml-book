# Compare too-small, just-right, and too-large learning rates on 1D quadratic
import numpy as np
import matplotlib.pyplot as plt

def error(g): return (g - 3)**2
def grad(g):  return 2*(g - 3)

def run(lr, steps=20):
    g = 8.0
    hist = [g]
    for _ in range(steps):
        g = g - lr*grad(g)
        hist.append(g)
    return hist

paths = {
    "small (0.02)": run(0.02, 60),
    "just right (0.1)": run(0.1, 30),
    "too large (0.8)": run(0.8, 15),
}

# plot position vs step
plt.figure(figsize=(8,5))
for name, hist in paths.items():
    plt.plot(range(len(hist)), hist, label=name)
plt.title("Learning Rate Comparison (position over steps)")
plt.xlabel("step"); plt.ylabel("guess")
plt.grid(True, linestyle=":", alpha=0.6); plt.legend()
plt.show()
