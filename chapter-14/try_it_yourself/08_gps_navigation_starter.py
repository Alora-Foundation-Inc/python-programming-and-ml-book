import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

# City locations (coordinates represent miles from origin)
cities_data = {
    "Name": ["Downtown", "Airport", "University", "Mall", "Hospital"],
    "X": [0, 25, -10, 15, -8],
    "Y": [0, 15, 20, -12, -18]
}
df_cities = pd.DataFrame(cities_data)

print("City Locations Data:")
print(df_cities)

# TODO:
# 1) Plot all cities (scatter). Label each city.
# 2) Ask for two city names via input(); look up their coordinates.
# 3) Compute Euclidean distance between them.
# 4) Draw a line segment connecting those two points; display the distance on the chart.
# 5) (Advanced) From 'Downtown', compute distance to every other city.
# 6) (Very Advanced) "Trip planner": total distance to visit multiple cities in order.
