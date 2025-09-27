# Predict pizza price = a*size + b*toppings + c via gradient descent (MSE)
import numpy as np

# Data: size (inches), toppings, price
X = np.array([
    [10, 1],
    [12, 2],
    [14, 1],
    [16, 3],
    [18, 4],
], dtype=float)
y = np.array([12.0, 16.0, 16.5, 21.5, 26.0], dtype=float)  # some target prices

# params: w=[a,b], c=bias
w = np.zeros(2)
c = 0.0
lr = 0.001
epochs = 4000
n = len(X)

for _ in range(epochs):
    yhat = X.dot(w) + c
    err = yhat - y
    dw = (2/n) * X.T.dot(err)
    dc = (2/n) * np.sum(err)
    w -= lr*dw
    c -= lr*dc

print("Learned params: a(size)≈{:.3f}, b(toppings)≈{:.3f}, c≈{:.3f}".format(w[0], w[1], c))

# test prediction
test = np.array([16, 2], dtype=float)
pred = test.dot(w) + c
print("Predicted price for 16-inch, 2 toppings:", round(pred,2))
