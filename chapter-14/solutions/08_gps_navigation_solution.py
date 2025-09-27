import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

df = pd.DataFrame({
    "Name": ["Downtown", "Airport", "University", "Mall", "Hospital"],
    "X": [0, 25, -10, 15, -8],
    "Y": [0, 15, 20, -12, -18]
})

def distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

print(df)

# Plot cities
plt.figure(figsize=(6,6))
for _, r in df.iterrows():
    plt.scatter(r["X"], r["Y"], s=120)
    plt.text(r["X"]+0.4, r["Y"]+0.4, r["Name"])

# Example: Airport to Hospital
pA = df.loc[df["Name"]=="Airport", ["X","Y"]].values[0]
pB = df.loc[df["Name"]=="Hospital", ["X","Y"]].values[0]
d = distance(pA, pB)
plt.plot([pA[0], pB[0]], [pA[1], pB[1]], linestyle="--")
plt.text((pA[0]+pB[0])/2, (pA[1]+pB[1])/2, f"{d:.2f} mi")

plt.axhline(0); plt.axvline(0)
plt.xlim(-20,30); plt.ylim(-25,25); plt.gca().set_aspect('equal', adjustable='box')
plt.title("GPS Navigation — Distance Example")
plt.xlabel("x (miles)"); plt.ylabel("y (miles)"); plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
