# Best-fit intuition: compare two lines on the same scatter to see which fits better
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [3,5,6,7,11,10,13,15]  # a bit noisy

plt.figure(figsize=(7,5))
plt.scatter(x, y, s=100, label="Data" )

# two candidate lines
xs = list(range(1,9))
line_a = [1.5*t + 0.5 for t in xs]   # closer
line_b = [1.0*t + 0.0 for t in xs]   # worse

plt.plot(xs, line_a, label="Better fit (y=1.5x+0.5)")
plt.plot(xs, line_b, label="Worse fit (y=x)")
plt.title("Which Line Fits Better?")
plt.xlabel("x"); plt.ylabel("y")
plt.grid(True, linestyle=":", alpha=0.6); plt.legend()
plt.show()
