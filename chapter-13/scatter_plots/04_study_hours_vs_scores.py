import pandas as pd
import matplotlib.pyplot as plt

hours=[1,2,2,3,3,4,5,6,6,7,8]
scores=[60,62,65,68,70,72,78,80,85,88,92]
df=pd.DataFrame({'Hours':hours,'Score':scores})
ax=df.plot.scatter(x='Hours', y='Score', s=100, figsize=(7,5), title='Study Hours vs Score')
# trendline
m=((df['Hours']*df['Score']).sum()-len(df)*df['Hours'].mean()*df['Score'].mean())/((df['Hours']**2).sum()-len(df)*(df['Hours'].mean()**2))
b=df['Score'].mean()-m*df['Hours'].mean()
xs=sorted(df['Hours'].unique()); ys=[m*x+b for x in xs]
plt.plot(xs, ys, linestyle='--')
plt.grid(axis='both', linestyle=':', alpha=0.6)
plt.show()
