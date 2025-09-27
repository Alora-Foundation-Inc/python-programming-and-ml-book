import matplotlib.pyplot as plt
import math

p1 = (-3, 1)
p2 = (4, 5)

# Distance formula (Euclidean)
dx = p2[0]-p1[0]
dy = p2[1]-p1[1]
dist = math.sqrt(dx*dx + dy*dy)

print(f"Points: P1{p1}, P2{p2}")
print("dx =", dx, "dy =", dy, "distance =", round(dist, 3))

plt.figure(figsize=(6,6))
plt.scatter([p1[0], p2[0]], [p1[1], p2[1]], s=120)
plt.plot([p1[0], p2[0]], [p1[1], p2[1]], linestyle="--")

# right triangle legs for visualization
plt.plot([p1[0], p2[0]], [p1[1], p1[1]])
plt.plot([p2[0], p2[0]], [p1[1], p2[1]])

plt.text((p1[0]+p2[0])/2, (p1[1]+p2[1])/2, f"d ≈ {dist:.2f}")
plt.axhline(0); plt.axvline(0)
plt.xlim(-6,6); plt.ylim(-2,8); plt.gca().set_aspect('equal', adjustable='box')
plt.title("Distance Between Two Points")
plt.xlabel("x"); plt.ylabel("y"); plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
