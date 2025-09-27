import pandas as pd
import matplotlib.pyplot as plt

names   = ["Alex", "Ben", "Cara", "Dana", "Eli"]
heights = [58, 62, 55, 60, 64]

df = pd.DataFrame({"Name": names, "Height": heights})
print(df)

plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Height"])
plt.title("Student Heights (Matplotlib)")
plt.xlabel("Student"); plt.ylabel("Height (inches)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
