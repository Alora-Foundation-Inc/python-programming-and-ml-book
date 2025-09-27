# Multivariate linear model with numpy (no sklearn)
import numpy as np

# Features: [size_inches, toppings]
X = np.array([
    [10, 1],
    [12, 2],
    [14, 1],
    [16, 3],
    [18, 4],
], dtype=float)
# Price = 6 + 0.5*size + 2*toppings
true_w = np.array([0.5, 2.0])
true_b = 6.0
y = X.dot(true_w) + true_b

# Learn w, b by least squares using augmented matrix
X_aug = np.hstack([X, np.ones((len(X),1))])
w_aug, *_ = np.linalg.lstsq(X_aug, y, rcond=None)
w_learned = w_aug[:2]; b_learned = w_aug[2]
print("Learned weights ~", w_learned, "bias ~", round(b_learned,2))

# Predict: 16-inch, 5 toppings
x_new = np.array([16,5], dtype=float)
pred = x_new.dot(w_learned) + b_learned
print("Predicted price (16", 5 toppings): $", round(pred,2))
