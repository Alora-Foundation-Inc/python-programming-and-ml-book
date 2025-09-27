import pandas as pd
import matplotlib.pyplot as plt

months  = ["Jan","Feb","Mar","Apr","May","Jun"]
heights = [48.2, 48.4, 48.7, 49.0, 49.2, 49.5]

df = pd.DataFrame({"Month": months, "Height": heights})
df["Growth"] = df["Height"].diff()
avg_growth = df["Growth"][1:].mean()
pred_july = df["Height"].iloc[-1] + avg_growth

print(df, "\nAverage monthly growth:", round(avg_growth,3), "inches")
print("Predicted July height:", round(pred_july,2))

plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Height"], marker="o", label="Measured")
plt.plot(["Jul"], [pred_july], marker="o", linestyle=":", label="Predicted (Jul)")
plt.title("Growth Over Time")
plt.xlabel("Month"); plt.ylabel("Height (inches)"); plt.legend(); plt.grid(axis='y', linestyle=':')
plt.show()
