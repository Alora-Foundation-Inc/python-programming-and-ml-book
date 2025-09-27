import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

months = [1,2,3,4,5,6,7,8]
sales  = [120,135,150,160,175,190,210,230]

df = pd.DataFrame({"Month": months, "Sales": sales})

# Linear Regression to fit y = m x + b
res = linregress(df["Month"], df["Sales"])
m, b = res.slope, res.intercept
print("Trend line: y = {:.2f}x + {:.2f}".format(m, b))

# Predict month 12
pred_x = 12
pred_y = m*pred_x + b
print("Predicted sales at month 12:", round(pred_y,1))

plt.figure(figsize=(8,5))
plt.scatter(df["Month"], df["Sales"], s=80, label="Actual")
xs = list(range(1,13))
ys = [m*x + b for x in xs]
plt.plot(xs, ys, linestyle="--", label="Trend")
plt.scatter([pred_x], [pred_y], marker="o", label="Pred @12")
plt.title("Sales Trend using Linear Equation")
plt.xlabel("Month"); plt.ylabel("Sales"); plt.grid(axis='y', linestyle=":", alpha=0.6)
plt.legend()
plt.show()
