import matplotlib.pyplot as plt
import math

A = (1, 3)
B = (5, 6)
C = (2, -1)

def dist(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

print("d(A,B) =", round(dist(A,B), 3))
print("d(A,C) =", round(dist(A,C), 3))

plt.figure(figsize=(5,5))
for name, p in [('A',A),('B',B),('C',C)]:
    plt.scatter(p[0], p[1], s=100)
    plt.text(p[0]+0.1, p[1]+0.1, name)
plt.axhline(0); plt.axvline(0)
plt.grid(True, linestyle=':', alpha=0.6); plt.gca().set_aspect('equal','box')
plt.title('2D Euclidean Distance')
plt.show()
