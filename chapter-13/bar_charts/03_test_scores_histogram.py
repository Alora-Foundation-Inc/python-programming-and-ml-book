import pandas as pd
import matplotlib.pyplot as plt

scores=[55,60,62,66,68,70,72,72,75,78,80,81,84,85,88,90,92,95,98]
s=pd.Series(scores)
print('Mean:', round(s.mean(),1), 'Median:', s.median())
plt.figure(figsize=(8,5))
plt.hist(s, bins=[50,60,70,80,90,100], edgecolor='black')
plt.title('Test Scores — Histogram')
plt.xlabel('Score'); plt.ylabel('Students')
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.show()
