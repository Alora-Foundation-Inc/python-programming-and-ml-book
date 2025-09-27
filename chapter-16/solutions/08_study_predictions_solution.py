import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({'Study_Hours':[1,2,3,4,5],'Test_Score':[65,70,75,80,85]})

try:
    from scipy.stats import linregress
    res = linregress(df['Study_Hours'], df['Test_Score'])
    m, b = res.slope, res.intercept
except Exception:
    m, b = np.polyfit(df['Study_Hours'], df['Test_Score'], 1)

print(f"Equation: score = {m:.2f} * hours + {b:.2f}")

h1, h2 = 3.5, 7
p1, p2 = m*h1 + b, m*h2 + b
print(f"Pred(3.5h) ≈ {p1:.1f}") 
print(f"Pred(7h)   ≈ {p2:.1f}  (extrapolation)")

plt.figure(figsize=(7,5))
plt.scatter(df['Study_Hours'], df['Test_Score'], s=100, label='Data')
xs = np.linspace(df['Study_Hours'].min(), df['Study_Hours'].max(), 100)
ys = m*xs + b
plt.plot(xs, ys, linestyle='--', label='Best‑fit line')
plt.scatter([h1,h2],[p1,p2], s=120, label='Predictions')
plt.title('Study Hours → Score'); plt.xlabel('Hours'); plt.ylabel('Score')
plt.grid(True, linestyle=':', alpha=0.6); plt.legend()
plt.show()
