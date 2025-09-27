import pandas as pd
import matplotlib.pyplot as plt

subjects=['Math','Science','History','Art','PE']
votes=[18,24,12,20,16]
df=pd.DataFrame({'Subject':subjects,'Votes':votes}).sort_values('Votes')
print(df)
plt.figure(figsize=(7,5))
plt.barh(df['Subject'], df['Votes'])
plt.title('Favorite Subject Votes (Horizontal Bar)')
plt.xlabel('Votes'); plt.ylabel('Subject')
plt.grid(axis='x', linestyle=':', alpha=0.6)
plt.tight_layout(); plt.show()
