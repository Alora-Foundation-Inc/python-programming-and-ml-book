import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({
    'Car_Age_Years':[1,3,5,7,10,2,8,12,6,4],
    'Miles_Per_Gallon':[35,32,28,25,20,34,23,18,27,30]
})

try:
    from scipy.stats import linregress
    res = linregress(df['Car_Age_Years'], df['Miles_Per_Gallon'])
    m, b = res.slope, res.intercept
except Exception:
    m, b = np.polyfit(df['Car_Age_Years'], df['Miles_Per_Gallon'], 1)

print(f"MPG ≈ {m:.2f}*Age + {b:.2f}  (slope is per‑year change)")

age_pred = 15
mpg_pred = m*age_pred + b
print(f"Predicted MPG at age {age_pred}: {mpg_pred:.1f}")

plt.figure(figsize=(8,5))
plt.scatter(df['Car_Age_Years'], df['Miles_Per_Gallon'], s=100, label='Data')
xs = np.linspace(df['Car_Age_Years'].min(), df['Car_Age_Years'].max(), 100)
ys = m*xs + b
plt.plot(xs, ys, linestyle='--', label='Best‑fit line')
plt.scatter([age_pred],[mpg_pred], s=120, label=f'Pred @ {age_pred}y')
plt.title('Car Age vs Fuel Efficiency'); plt.xlabel('Age (years)'); plt.ylabel('MPG')
plt.grid(True, linestyle=':', alpha=0.6); plt.legend()
plt.show()

print('Implication: Older cars tend to use more fuel (lower MPG) → more emissions.')
