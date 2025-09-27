import pandas as pd
import matplotlib.pyplot as plt

scores = [95, 87, 92, 78, 85, 91, 76, 88, 94, 82, 89, 77, 93, 86, 90]
s = pd.Series(scores)
bins = [0,60,70,80,90,100.001]
labels = ["F","D","C","B","A"]
cats = pd.cut(s, bins=bins, labels=labels, right=False, include_lowest=True)
counts = cats.value_counts().sort_index()
perc = (counts/len(s))*100
print("Counts:
", counts, "
Percentages (%):
", perc.round(1))
print("Mean:", round(s.mean(),1), "Median:", s.median())

plt.figure(figsize=(8,5))
plt.bar(counts.index, counts.values)
plt.title("Grade Distribution")
plt.xlabel("Grade"); plt.ylabel("Count"); plt.grid(axis='y', linestyle=':')
plt.show()
