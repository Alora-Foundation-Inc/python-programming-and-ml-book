import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
fig=plt.figure(figsize=(12,4))
# positive
x1=np.linspace(0,10,30); y1=2*x1+np.random.normal(0,2,len(x1))
ax1=fig.add_subplot(1,3,1); ax1.scatter(x1,y1); ax1.set_title('Positive correlation')
# none
x2=np.linspace(0,10,30); y2=np.random.normal(0,5,len(x2))+50
ax2=fig.add_subplot(1,3,2); ax2.scatter(x2,y2); ax2.set_title('No clear correlation')
# negative
x3=np.linspace(0,10,30); y3=-2*x3+30+np.random.normal(0,2,len(x3))
ax3=fig.add_subplot(1,3,3); ax3.scatter(x3,y3); ax3.set_title('Negative correlation')
for ax in [ax1,ax2,ax3]:
    ax.grid(True, linestyle=':', alpha=0.6); ax.set_xlabel('X'); ax.set_ylabel('Y')
plt.tight_layout(); plt.show()
