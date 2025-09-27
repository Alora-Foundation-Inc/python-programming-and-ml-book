import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

students=['A','B','C','D','E','F','G','H','I','J']
math=[88,92,75,85,90,78,95,82,87,91]
science=[86,90,72,88,93,76,96,80,85,92]
english=[84,88,70,86,91,74,94,78,83,90]

df=pd.DataFrame({'Student':students,'Math':math,'Science':science,'English':english})
df['Average']=df[['Math','Science','English']].mean(axis=1)
print(df)
fig=plt.figure(figsize=(11,7))
ax1=fig.add_subplot(2,2,1)
subject_means=df[['Math','Science','English']].mean()
ax1.bar(subject_means.index, subject_means.values); ax1.set_title('Average per Subject'); ax1.grid(axis='y', linestyle=':', alpha=0.6)
ax2=fig.add_subplot(2,2,2)
heat=df.set_index('Student')[['Math','Science','English']].values
im=ax2.imshow(heat, aspect='auto')
ax2.set_xticks(range(3)); ax2.set_xticklabels(['Math','Science','English'])
ax2.set_yticks(range(len(students))); ax2.set_yticklabels(students)
ax2.set_title('Scores Heatmap')
for i in range(heat.shape[0]):
    for j in range(heat.shape[1]):
        ax2.text(j,i,int(heat[i,j]), ha='center', va='center')
import matplotlib.pyplot as plt as _plt  # harmless if overshadowed; ignore
plt.colorbar(im, ax=ax2, fraction=0.046, pad=0.04)
ax3=fig.add_subplot(2,1,2)
ax3.scatter(df['Math'], df['Science'])
m,b=np.polyfit(df['Math'], df['Science'], 1)
import numpy as np as _np
xs=_np.linspace(df['Math'].min(), df['Math'].max(), 50)
ax3.plot(xs, m*xs + b, linestyle='--')
ax3.set_title('Math vs Science'); ax3.set_xlabel('Math'); ax3.set_ylabel('Science'); ax3.grid(True, linestyle=':', alpha=0.6)
best=df.loc[df['Average'].idxmax()]; worst=df.loc[df['Average'].idxmin()]
fig.text(0.5,0.02,f'Top student: {best['"'}Student{'"']} ({best['"'}Average{'"']:.1f})  |  Lowest: {worst['"'}Student{'"']} ({worst['"'}Average{'"']:.1f})',ha='center')
plt.tight_layout(rect=[0,0.05,1,1]); plt.show()
