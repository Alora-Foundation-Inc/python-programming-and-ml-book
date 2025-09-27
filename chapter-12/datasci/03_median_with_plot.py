import pandas as pd
import matplotlib.pyplot as plt

scores_odd  = [85, 92, 78, 88, 95, 82, 90]
scores_even = [85, 92, 78, 88, 95, 82, 90, 75]

med_odd  = pd.Series(scores_odd).median()
med_even = pd.Series(scores_even).median()

print("Median (odd):", med_odd)
print("Median (even):", med_even)

plt.figure(figsize=(8,5))
plt.scatter(range(len(scores_odd)), sorted(scores_odd), s=100, label="Scores (sorted)")
plt.axhline(y=med_odd, linewidth=3, label=f"Median: {med_odd}")
plt.title("Median (Odd Count)")
plt.xlabel("Position after sort"); plt.ylabel("Score")
plt.xticks(range(len(scores_odd)))
plt.grid(axis='y', linestyle=':')
plt.legend()
plt.show()
