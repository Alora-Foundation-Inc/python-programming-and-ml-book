import numpy as np

# A few sequences with hidden patterns. Fill the '?'.
sequences = [
    {"name":"Even Numbers",       "data":[2, 4, 6, 8, np.nan]},     # +2
    {"name":"Perfect Squares",    "data":[1, 4, 9, 16, np.nan]},    # n^2
    {"name":"Fibonacci",          "data":[1, 1, 2, 3, 5, np.nan]},  # a+b
    {"name":"Subtract Three",     "data":[10, 7, 4, 1, np.nan]},    # -3
]

# TODOs:
# 1) Show the numbers and ask the user to guess the missing value (use input()).
# 2) Compute the real next number using simple rules you write.
# 3) Check guess vs answer; keep score across all sequences.
# 4) Print a final score and short explanation of each pattern.
