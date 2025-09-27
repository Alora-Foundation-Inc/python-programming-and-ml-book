import pandas as pd
import matplotlib.pyplot as plt

days=list(range(1,8))
highs=[70,72,71,75,77,80,78]
lows=[55,56,54,57,59,60,58]
df=pd.DataFrame({'Day':days,'High':highs,'Low':lows})
plt.figure(figsize=(8,5))
plt.plot(df['Day'], df['High'], marker='o', label='High')
plt.plot(df['Day'], df['Low'], marker='o', linestyle='--', label='Low')
plt.title('Daily Temperatures (Week)')
plt.xlabel('Day'); plt.ylabel('°F')
plt.legend(); plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.show()
