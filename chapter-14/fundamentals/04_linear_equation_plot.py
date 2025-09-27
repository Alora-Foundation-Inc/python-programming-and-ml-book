import matplotlib.pyplot as plt

# y = m x + b
m = 0.5   # slope
b = 1.0   # y-intercept

xs = [x/2 for x in range(-12, 13)]  # -6 to 6 in steps of 0.5
ys = [m*x + b for x in xs]

print(f"Line: y = {m}x + {b}")

plt.figure(figsize=(6,6))
plt.plot(xs, ys)
plt.axhline(0); plt.axvline(0)
plt.xlim(-6,6); plt.ylim(-6,6); plt.gca().set_aspect('equal', adjustable='box')
plt.title("Plotting a Linear Equation: y = m x + b")
plt.xlabel("x"); plt.ylabel("y"); plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
