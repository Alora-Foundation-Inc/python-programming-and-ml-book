import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({
    'Hours_Practiced':[10,25,40,55,70,15,30,60,45,20],
    'Free_Throw_Percentage':[45,60,72,80,85,50,65,82,75,55]
})

try:
    from scipy.stats import linregress
    res = linregress(df['Hours_Practiced'], df['Free_Throw_Percentage'])
    m, b = res.slope, res.intercept
except Exception:
    m, b = np.polyfit(df['Hours_Practiced'], df['Free_Throw_Percentage'], 1)

print(f"FT% ≈ {m:.3f}*Hours + {b:.3f}")
h_pred = 100
p_pred = m*h_pred + b
print(f"Predicted FT% at {h_pred} hours ≈ {p_pred:.1f}")

plt.figure(figsize=(8,5))
plt.scatter(df['Hours_Practiced'], df['Free_Throw_Percentage'], s=100, label='Data')
xs = np.linspace(df['Hours_Practiced'].min(), df['Hours_Practiced'].max(), 100)
ys = m*xs + b
plt.plot(xs, ys, linestyle='--', label='Best‑fit line')
plt.scatter([h_pred],[p_pred], s=120, label=f'Pred @ {h_pred}h')
plt.title('Practice Hours vs Free‑Throw %'); plt.xlabel('Hours'); plt.ylabel('FT %')
plt.grid(True, linestyle=':', alpha=0.6); plt.legend()
plt.show()

print('Reality check: Skills often plateau — linear growth may over‑predict at high hours.')
