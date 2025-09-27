import pandas as pd
import matplotlib.pyplot as plt

data = [10, 12, 15, 18, 20, 5, 25]
s = pd.Series(data)
m = s.mean(); sd = s.std()
print("Mean:", round(m,2), "Std Dev:", round(sd,2))

plt.figure(figsize=(10,6))
plt.scatter(range(len(data)), data, s=150, label="Data points")
plt.axhline(y=m, linestyle='--', linewidth=2, label=f"Mean = {m:.2f}")
plt.axhspan(m-sd, m+sd, alpha=0.1, label="±1 SD")
for i, v in enumerate(data): plt.text(i, v+1.5, str(v), ha='center')
plt.title("Standard Deviation — How far from the mean?")
plt.ylabel("Value"); plt.xticks([]); plt.legend(); plt.grid(axis='y', linestyle=':')
plt.show()
