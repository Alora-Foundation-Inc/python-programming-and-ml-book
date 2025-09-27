import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'Input':[1,2,3,4,5],'Output':[3,5,7,9,11]})
m = 2
b = 1
pred_x = 6
pred_y = m*pred_x + b

print(f"Equation: Output = {m}*Input + {b}")
print(f"Prediction for Input=6: {pred_y}")

plt.figure(figsize=(7,5))
plt.scatter(df['Input'], df['Output'], s=100, label="Data")
xs = list(range(1,7))
ys = [m*x + b for x in xs]
plt.plot(xs, ys, linestyle="--", label="Model")
plt.scatter([pred_x],[pred_y], s=120, label=f"Pred(6)={pred_y}")
plt.title("Pattern Detective — Solution")
plt.xlabel("Input"); plt.ylabel("Output"); plt.grid(True, linestyle=":"); plt.legend()
plt.show()
