import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

# Simple "city map" with coordinates (miles from origin)
cities = {
    "Name": ["Downtown", "Airport", "University", "Mall", "Hospital"],
    "X":    [0, 25, -10, 15, -8],
    "Y":    [0, 15, 20, -12, -18],
}
df = pd.DataFrame(cities)

def dist(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

origin = df.loc[df["Name"]=="Downtown", ["X","Y"]].values[0]
df["DistanceFromDowntown"] = [dist(origin, (x,y)) for x,y in df[["X","Y"]].values]
print(df)

plt.figure(figsize=(6,6))
for _, row in df.iterrows():
    plt.scatter(row["X"], row["Y"], s=120)
    plt.text(row["X"]+0.5, row["Y"]+0.5, row["Name"])

plt.axhline(0); plt.axvline(0)
plt.xlim(-20,30); plt.ylim(-25,25); plt.gca().set_aspect('equal', adjustable='box')
plt.title("Emergency Distance Map — from Downtown")
plt.xlabel("x (miles)"); plt.ylabel("y (miles)"); plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
