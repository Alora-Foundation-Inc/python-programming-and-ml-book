import pandas as pd
import matplotlib.pyplot as plt

games=['Mario','Zelda','Minecraft','Fortnite','Among Us']
sales=[40,25,200,80,15]
df=pd.DataFrame({'Game':games,'Sales (M)':sales})
print(df)
plt.figure(figsize=(8,5))
plt.bar(df['Game'], df['Sales (M)'])
plt.title('Video Game Sales (millions)')
plt.xlabel('Game'); plt.ylabel('Sales (M)')
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.show()
