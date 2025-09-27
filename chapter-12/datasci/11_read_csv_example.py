import pandas as pd

try:
    df = pd.read_csv("daily_temperatures.csv")
    print("Loaded CSV:")
    print(df.head())
    print("\nAvg temp:", round(df["Temperature_F"].mean(),1))
    print("Max humidity:", df["Humidity_percent"].max())
except FileNotFoundError:
    print("daily_temperatures.csv not found. Place it next to this script and try again.")
