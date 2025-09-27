import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

df = pd.DataFrame({
    'Distance_Feet': [5, 8, 12, 15, 18, 20, 25, 30],
    'Shooting_Percentage': [85, 78, 65, 58, 45, 40, 30, 25]
})

x = df['Distance_Feet'].values
y = df['Shooting_Percentage'].values
m, b, *_ = linregress(x, y)
print(f"Best-fit: shooting% = {m:.2f}*distance + {b:.2f}")

plt.figure(figsize=(8,5))
plt.scatter(x, y, s=80, label="Player")
xs = np.linspace(x.min(), x.max(), 100)
plt.plot(xs, m*xs + b, linestyle="--", label="Best-fit line")

# Predictions
for d in [10, 22]:
    yhat = m*d + b
    plt.scatter([d], [yhat], marker="o")
    plt.text(d+0.3, yhat+1.0, f"{yhat:.1f}% @ {d}ft")

plt.title("Sports Analytics — Distance vs Shooting%")
plt.xlabel("Distance (feet)"); plt.ylabel("Shooting %")
plt.grid(True, linestyle=":", alpha=0.6); plt.legend()
plt.show()
