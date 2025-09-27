import matplotlib.pyplot as plt

# Left: regression line; Right: classification groups (toy)
fig = plt.figure(figsize=(10,4))

# Regression
ax1 = fig.add_subplot(1,2,1)
x = [1,2,3,4,5,6]
y = [2,3,5,7,8,10]
ax1.scatter(x,y, s=60)
ax1.plot(x, [1.5*t for t in x], linestyle='--')
ax1.set_title('Regression: predict a NUMBER')
ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.grid(True, linestyle=':', alpha=0.6)

# Classification (two classes)
ax2 = fig.add_subplot(1,2,2)
red  = [(1,1),(2,1),(2,2),(3,2)]
blue = [(4,4),(5,4),(5,5),(6,5)]
ax2.scatter([a for a,b in red],[b for a,b in red], s=80, label='Red (0)')
ax2.scatter([a for a,b in blue],[b for a,b in blue], s=80, label='Blue (1)')
ax2.set_title('Classification: predict a LABEL')
ax2.set_xlabel('x'); ax2.set_ylabel('y'); ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend()
plt.tight_layout(); plt.show()
