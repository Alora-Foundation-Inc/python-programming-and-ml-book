# Learn y = m x + b by gradient descent on tiny data (no sklearn)
import numpy as np

x = np.array([1,2,3,4,5], dtype=float)
y = np.array([3,5,7,9,11], dtype=float)  # true m=2, b=1

m, b = 0.0, 0.0            # random-ish guess
lr = 0.02                  # learning rate
epochs = 400

for _ in range(epochs):
    y_pred = m*x + b
    # mean squared error gradients
    dm = (2/len(x)) * ((y_pred - y) * x).sum()
    db = (2/len(x)) * (y_pred - y).sum()
    m -= lr*dm
    b -= lr*db

print(f"Learned m ≈ {m:.2f}, b ≈ {b:.2f}")  # should be close to 2 and 1
