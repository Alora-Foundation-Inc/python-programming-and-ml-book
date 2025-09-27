import matplotlib.pyplot as plt

# Example line through (x1,y1) and (x2,y2)
x1, y1 = -2, -1
x2, y2 = 4, 2

m = (y2 - y1) / (x2 - x1)  # slope
print("Slope m = (y2 - y1)/(x2 - x1) =", round(m, 3))

xs = [x1, x2]
ys = [y1, y2]

plt.figure(figsize=(6,6))
plt.plot(xs, ys, marker="o")
plt.text(x1, y1-0.5, f"({x1},{y1})")
plt.text(x2, y2+0.2, f"({x2},{y2})")
plt.axhline(0); plt.axvline(0)
plt.xlim(-6,6); plt.ylim(-6,6); plt.gca().set_aspect('equal', adjustable='box')
plt.title("Understanding Slope (Rise over Run)")
plt.xlabel("x"); plt.ylabel("y"); plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
