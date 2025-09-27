import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

teams=['Lions','Bears','Tigers','Wolves','Hawks']
wins=[8,10,6,12,9]
points=[240,260,210,300,255]
allowed=[200,230,220,240,245]

df=pd.DataFrame({'Team':teams,'Wins':wins,'PointsFor':points,'PointsAllowed':allowed})
fig=plt.figure(figsize=(10,7))
ax1=fig.add_subplot(2,2,1)
ax1.bar(df['Team'], df['Wins'])
ax1.set_title('Team Wins'); ax1.set_ylabel('Wins'); ax1.grid(axis='y', linestyle=':', alpha=0.6)
ax2=fig.add_subplot(2,2,2)
ax2.scatter(df['PointsFor'], df['PointsAllowed'])
lims=[min(points+allowed)-10, max(points+allowed)+10]
ax2.plot(lims, lims, linestyle='--')
ax2.set_xlim(lims); ax2.set_ylim(lims)
ax2.set_title('Points For vs Allowed'); ax2.set_xlabel('Points For'); ax2.set_ylabel('Points Allowed')
ax2.grid(True, linestyle=':', alpha=0.6)
ax3=fig.add_subplot(2,1,2)
df_sorted=df.sort_values('Wins')
ax3.plot(df_sorted['Team'], df_sorted['Wins'].cumsum(), marker='o')
ax3.set_title('Cumulative Wins (sorted)'); ax3.set_xlabel('Team (sorted)'); ax3.set_ylabel('Cumulative Wins')
ax3.grid(axis='y', linestyle=':', alpha=0.6)
best_offense=df.loc[df['PointsFor'].idxmax(),'Team']
best_defense=df.loc[df['PointsAllowed'].idxmin(),'Team']
fig.text(0.52,0.03,f'Best offense: {best_offense}  |  Best defense: {best_defense}',ha='center')
plt.tight_layout(rect=[0,0.05,1,1]); plt.show()
