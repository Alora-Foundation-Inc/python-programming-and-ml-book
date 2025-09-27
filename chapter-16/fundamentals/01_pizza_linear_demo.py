# Pizza party cost vs guests — exact linear relationship: cost = 4*guests + 5
import matplotlib.pyplot as plt

guests = [5, 10, 15]
costs  = [25, 45, 65]  # +$4 per guest, $5 base

m = 4   # dollars per guest
b = 5   # base cost

print(f"Equation: cost = {m} * guests + {b}")
pred_guests = 18
pred_cost = m*pred_guests + b
print(f"Prediction for {pred_guests} guests: ${pred_cost}")

plt.figure(figsize=(7,5))
plt.scatter(guests, costs, s=120, label="Past parties")
xs = list(range(0, 22))
ys = [m*x + b for x in xs]
plt.plot(xs, ys, linestyle="--", label="Line: cost = 4*guests + 5")
plt.scatter([pred_guests], [pred_cost], s=120, label=f"Pred @ {pred_guests} guests = ${pred_cost}")
plt.title("Pizza Party Cost — Linear Relationship") 
plt.xlabel("Guests"); plt.ylabel("Cost ($)")
plt.grid(True, linestyle=":", alpha=0.6); plt.legend()
plt.show()
