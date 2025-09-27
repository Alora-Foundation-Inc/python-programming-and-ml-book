import pandas as pd
import matplotlib.pyplot as plt

months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
temp_c=[4,5,7,10,14,18,20,20,17,12,8,5]
aqi=[60,58,55,50,45,40,38,39,42,50,55,58]
rain=[60,50,55,45,50,60,65,70,55,50,55,60]

df=pd.DataFrame({'Month':months,'TempC':temp_c,'AQI':aqi,'RainMM':rain})
fig,ax=plt.subplots(2,2, figsize=(10,7))
ax[0,0].plot(df['Month'], df['TempC'], marker='o'); ax[0,0].set_title('Temperature (°C)'); ax[0,0].grid(axis='y', linestyle=':', alpha=0.6)
ax[0,1].plot(df['Month'], df['AQI'], marker='o', linestyle='--'); ax[0,1].set_title('Air Quality Index (lower is better)'); ax[0,1].grid(axis='y', linestyle=':', alpha=0.6)
ax[1,0].bar(df['Month'], df['RainMM']); ax[1,0].set_title('Rainfall (mm)'); ax[1,0].grid(axis='y', linestyle=':', alpha=0.6)
ax[1,1].scatter(df['TempC'], df['AQI']); ax[1,1].set_title('Temp vs AQI'); ax[1,1].set_xlabel('Temp (°C)'); ax[1,1].set_ylabel('AQI'); ax[1,1].grid(True, linestyle=':', alpha=0.6)
avg_temp=df['TempC'].mean(); avg_aqi=df['AQI'].mean(); total_rain=df['RainMM'].sum()
fig.text(0.5,0.02,f'Avg Temp: {avg_temp:.1f}°C | Avg AQI: {avg_aqi:.0f} | Total Rain: {total_rain} mm',ha='center')
plt.tight_layout(rect=[0,0.05,1,1]); plt.show()
