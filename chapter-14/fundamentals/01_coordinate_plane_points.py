import matplotlib.pyplot as plt

# Simple points on the coordinate plane
points = {
    "A": (0, 0),
    "B": (3, 2),
    "C": (-4, 1),
    "D": (2, -3),
    "E": (-2, -2)
}

plt.figure(figsize=(6,6))

for name, (x,y) in points.items():
    plt.scatter(x, y, s=100)
    plt.text(x+0.1, y+0.1, name)

# x/y axes
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)
plt.xlim(-6,6); plt.ylim(-6,6)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Coordinate Plane — Plotting Points")
plt.xlabel("x"); plt.ylabel("y"); plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
