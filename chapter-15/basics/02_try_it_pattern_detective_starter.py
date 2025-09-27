import pandas as pd
import matplotlib.pyplot as plt

mystery_data = {
    'Input': [1, 2, 3, 4, 5],
    'Output': [3, 5, 7, 9, 11]
}
df = pd.DataFrame(mystery_data)
print("Mystery Data:\n", df)

# TODOs:
# 1) Plot Input vs Output points
# 2) Spot the pattern (it's linear): Output = m*Input + b
# 3) Find m and b
# 4) Predict Output when Input = 6
# 5) Plot your prediction on the graph
#
# Hint: The change in Output is constant (+2). What is b?
