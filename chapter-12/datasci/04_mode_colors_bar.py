import pandas as pd
import matplotlib.pyplot as plt

favorite_colors = ["red","blue","red","green","blue","red","yellow","red","blue"]
series = pd.Series(favorite_colors)
modes = series.mode()
print("Mode(s):", list(modes))

counts = series.value_counts()
plt.figure(figsize=(8,5))
plt.bar(counts.index, counts.values)
plt.title("Favorite Colors — Mode")
plt.xlabel("Color"); plt.ylabel("Count")
plt.grid(axis='y', linestyle=':')
plt.show()
