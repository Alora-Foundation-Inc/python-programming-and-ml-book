import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Study hours vs test score — fit a best-fit line (like Chapter 13)
hours = [1,2,2,3,3,4,5,6,6,7,8]
scores = [60,62,65,68,70,72,78,80,85,88,92]
df = pd.DataFrame({"Hours": hours, "Score": scores})

res = linregress(df["Hours"], df["Score"])
m, b, r = res.slope, res.intercept, res.rvalue
print("Best-fit line: score = {:.2f}*hours + {:.2f}".format(m,b))
print("Correlation r =", round(r,3))

plt.figure(figsize=(8,5))
plt.scatter(df["Hours"], df["Score"], s=80, label="Data")
xs = list(range(1,9))
ys = [m*x + b for x in xs]
plt.plot(xs, ys, linestyle="--", label="Best-fit")
plt.title("Linear Regression Demo")
plt.xlabel("Study Hours"); plt.ylabel("Score")
plt.grid(True, linestyle=":", alpha=0.6); plt.legend()
plt.show()
