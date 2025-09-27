import matplotlib.pyplot as plt

# Hours studied -> Score (simple linear pattern)
hours = [1,2,3,4,5,6]
scores = [50,60,70,80,90,100]

print("Pattern rule: +10 points per extra hour (Score = 10*Hours + 40)")

plt.figure(figsize=(7,5))
plt.scatter(hours, scores, s=100, label="Data")
plt.plot(hours, scores, linestyle="--", label="Pattern line")
plt.title("Learning from Examples: Hours vs Score")
plt.xlabel("Hours"); plt.ylabel("Score"); plt.grid(True, linestyle=":"); plt.legend()
plt.show()
