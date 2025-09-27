import matplotlib.pyplot as plt

values=[30,32,31,33]
fig=plt.figure(figsize=(10,4))
ax1=fig.add_subplot(1,2,1)
ax1.bar(range(len(values)), values)
ax1.set_title('BAD: Truncated Y-axis')
ax1.set_ylim(28,34)
ax2=fig.add_subplot(1,2,2)
ax2.bar(range(len(values)), values)
ax2.set_title('GOOD: Axis begins at zero')
ax2.set_ylim(0,34)
plt.tight_layout(); plt.show()
