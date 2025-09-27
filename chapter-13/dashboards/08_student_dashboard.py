import matplotlib.pyplot as plt

subjects=['Math','Science','History','Art','PE']
scores=[88,92,81,95,78]
homework=[5,4,3,6,2]

fig=plt.figure(figsize=(10,6))
ax1=fig.add_subplot(2,2,1)
ax1.bar(subjects, scores); ax1.set_title('Scores'); ax1.grid(axis='y', linestyle=':', alpha=0.6)
ax2=fig.add_subplot(2,2,2)
ax2.pie(homework, labels=subjects, autopct='%1.0f%%'); ax2.set_title('Homework Time Split')
ax3=fig.add_subplot(2,1,2)
ax3.scatter(homework, scores)
ax3.set_title('Homework Hours vs Score'); ax3.set_xlabel('Hours / week'); ax3.set_ylabel('Score')
ax3.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout(); plt.show()
