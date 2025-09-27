import pandas as pd
import matplotlib.pyplot as plt

scores = [55, 60, 65, 68, 70, 72, 75, 78, 80, 85, 90, 95, 100, 20, 120]  # with outliers
s = pd.Series(scores)
q1, q3 = s.quantile(0.25), s.quantile(0.75)
iqr = q3 - q1
print("Min:", s.min(), "Q1:", q1, "Median:", s.median(), "Q3:", q3, "Max:", s.max(), "IQR:", iqr)

plt.figure(figsize=(10,5))
plt.boxplot(scores, vert=False, patch_artist=True)
plt.title("Box Plot with IQR")
plt.xlabel("Score"); plt.yticks([]); plt.grid(axis='x', linestyle=':')
plt.show()
