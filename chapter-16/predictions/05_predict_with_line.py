# Predict using a learned line: Sales = 4*Temp - 260
import matplotlib.pyplot as plt

m, b = 4, -260
temps = [70, 72, 75, 80, 85]
sales = [20, 28, 40, 60, 80]  # just a toy sequence for reference plot

pred_temp = 77
pred_sales = m*pred_temp + b
print(f"Equation: sales = {m}*temp + ({b})  → Pred at {pred_temp}°F = {pred_sales}")

plt.figure(figsize=(7,5))
plt.scatter(temps, sales, s=100, label="Sample data")
xs = list(range(60, 91))
ys = [m*t + b for t in xs]
plt.plot(xs, ys, linestyle="--", label="Regression line") 
plt.scatter([pred_temp], [pred_sales], s=120, label=f"Pred @ {pred_temp}°F = {pred_sales}")
plt.title("Ice Cream Sales Prediction"); plt.xlabel("Temperature (°F)"); plt.ylabel("Sales (units)")
plt.grid(True, linestyle=":", alpha=0.6); plt.legend()
plt.show()
