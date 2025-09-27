import pandas as pd
import matplotlib.pyplot as plt

class_a = [75, 77, 78, 79, 80, 81, 82, 83, 85]
class_b = [60, 65, 75, 80, 85, 85, 90, 95, 100]

sa = pd.Series(class_a); sb = pd.Series(class_b)
ra = sa.max()-sa.min(); rb = sb.max()-sb.min()
print(f"Class A range: {ra} (min {sa.min()} to max {sa.max()})")
print(f"Class B range: {rb} (min {sb.min()} to max {sb.max()})")

plt.figure(figsize=(10,6))
plt.scatter(range(len(class_a)), class_a, s=100, label="Class A")
plt.hlines([sa.min(), sa.max()], -0.5, len(class_a)-0.5, linestyles=':')
plt.scatter([i+0.2 for i in range(len(class_b))], class_b, s=100, label="Class B")
plt.hlines([sb.min(), sb.max()], -0.3, len(class_b)-0.3, linestyles=':')
plt.title("Spread Comparison: Class A vs Class B")
plt.ylabel("Score"); plt.xticks([]); plt.legend()
plt.grid(axis='y', linestyle=':')
plt.show()
