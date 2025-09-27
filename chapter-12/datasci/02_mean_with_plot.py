import pandas as pd
import matplotlib.pyplot as plt

scores = [85, 92, 78, 88, 95, 82, 90]
s = pd.Series(scores)
mean_score = s.mean()
print("Mean:", round(mean_score,1))

plt.figure(figsize=(8,5))
plt.scatter(range(len(scores)), scores, s=100, label="Scores")
plt.axhline(y=mean_score, linewidth=3, linestyle='--', label=f"Mean: {mean_score:.1f}")
plt.title("Test Scores with Mean Line")
plt.xlabel("Student (index)"); plt.ylabel("Score")
plt.xticks(range(len(scores)), [f"S{i+1}" for i in range(len(scores))])
plt.grid(axis='y', linestyle=':')
plt.legend()
plt.show()
