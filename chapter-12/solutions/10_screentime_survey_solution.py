import pandas as pd
import matplotlib.pyplot as plt

responses = [6,4,8,3,7,5,9,2,6,4,7,8,5,6,3,7,4,8,5,6]
s = pd.Series(responses)

mean = s.mean(); med = s.median(); mode = list(s.mode())
rng = s.max()-s.min(); sd = s.std()
print("Mean:", round(mean,2), "Median:", med, "Mode:", mode, "Range:", rng, "StdDev:", round(sd,2))

plt.figure(figsize=(8,5))
plt.hist(s, bins=[0,2,4,6,8,10], edgecolor="black")
plt.title("Daily Screen Time (hours)"); plt.xlabel("Hours"); plt.ylabel("Students")
plt.grid(axis='y', linestyle=':')
plt.show()

above_guideline = (s > 2).sum()
print(f"Students above 2 hours/day guideline: {above_guideline}/{len(s)}")
if mean > 2: print("On average, this group exceeds the recommended limit.")
else: print("On average, this group meets the recommended limit.")
