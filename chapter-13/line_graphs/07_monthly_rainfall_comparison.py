import pandas as pd
import matplotlib.pyplot as plt

months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
city_a=[3.1,3.0,3.5,3.8,4.1,4.3,4.0,3.9,3.6,3.3,3.2,3.1]
city_b=[2.0,2.2,2.8,3.2,3.7,4.0,4.4,4.1,3.5,2.8,2.4,2.1]

df=pd.DataFrame({'Month':months,'City A':city_a,'City B':city_b})
plt.figure(figsize=(9,5))
plt.plot(df['Month'], df['City A'], marker='o', label='City A')
plt.plot(df['Month'], df['City B'], marker='o', linestyle='--', label='City B')
plt.title('Monthly Rainfall — City A vs City B')
plt.xlabel('Month'); plt.ylabel('Inches')
plt.legend(); plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.show()
