# 1D gradient descent on Error = (guess - 3)^2
import numpy as np
import matplotlib.pyplot as plt

def error(g): return (g - 3)**2
def grad(g):  return 2*(g - 3)

g = 8.0              # start far away
lr = 0.1             # learning rate
history = [(0, g, error(g))]

for step in range(1, 31):
    g = g - lr*grad(g)
    history.append((step, g, error(g)))

for step, val, err in history[:6]:
    print(f"step {step:2d}  guess={val:.4f}  error={err:.6f}")
print("final:", history[-1])

# Plot error curve and the path of guesses
xs = np.linspace(-1, 7, 200)
ys = (xs - 3)**2
plt.figure(figsize=(7,5))
plt.plot(xs, ys)
plt.scatter([h[1] for h in history], [h[2] for h in history], s=80)
plt.title("1D Gradient Descent on (guess - 3)^2")
plt.xlabel("guess"); plt.ylabel("error")
plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
