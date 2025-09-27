# Tiny reinforcement learning demo: a 1D line world from x=-5 to x=+5
# Agent starts at -5, treasure at +5; hitting an obstacle at 0 gives a penalty.
# We simulate simple Q-learning with very few states and actions.

import numpy as np

states = list(range(-5,6))      # -5,-4,...,5
actions = [-1, +1]              # move left or right
start_state = -5
goal = 5
obstacle = 0

alpha = 0.4     # learning rate
gamma = 0.9     # discount
eps   = 0.2     # epsilon-greedy

Q = {(s,a): 0.0 for s in states for a in actions}

def reward(s_next):
    if s_next == goal: return +10
    if s_next == obstacle: return -5
    return -0.1  # small step cost

def step(s, a):
    s_next = max(min(s + a, goal), -5)
    r = reward(s_next)
    done = s_next == goal
    return s_next, r, done

def policy(s):
    if np.random.rand() < eps:
        return np.random.choice(actions)
    qs = [Q[(s,a)] for a in actions]
    return actions[int(np.argmax(qs))]

# Train
for episode in range(200):
    s = start_state
    done = False
    while not done:
        a = policy(s)
        s_next, r, done = step(s, a)
        # TD update
        best_next = max(Q[(s_next, a2)] for a2 in actions)
        Q[(s,a)] += alpha * (r + gamma*best_next - Q[(s,a)])
        s = s_next

# Test a greedy run
s = start_state
trajectory = [s]
while s != goal and len(trajectory) < 40:
    qs = [Q[(s,a)] for a in actions]
    a = actions[int(np.argmax(qs))]
    s, _, _ = step(s, a)
    trajectory.append(s)

print("Learned greedy path:", trajectory)
