# Study time vs score — find slope and intercept from neat data
import matplotlib.pyplot as plt

hours  = [2,4,6,8]
scores = [70,80,90,100]

# slope (rise/run) using first & last points
m = (scores[-1] - scores[0]) / (hours[-1] - hours[0])   # (100-70)/(8-2) = 30/6 = 5
# b from y = m x + b (use first point)
b = scores[0] - m*hours[0]  # 70 - 5*2 = 60
print(f"Equation: score = {m} * hours + {b}")

plt.figure(figsize=(7,5))
plt.scatter(hours, scores, s=120, label="Data")
xs = list(range(0,10))
ys = [m*x + b for x in xs]
plt.plot(xs, ys, linestyle="--", label=f"score = {m}*hours + {b}")
plt.title("Study Hours vs Test Score (Perfect Line)")
plt.xlabel("Hours studied"); plt.ylabel("Score")
plt.grid(True, linestyle=":", alpha=0.6); plt.legend()
plt.show()
