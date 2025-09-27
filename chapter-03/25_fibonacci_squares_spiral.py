import turtle

t = turtle.Turtle()
t.speed(8)
t.pensize(2)
colors = ["#e41a1c","#377eb8","#4daf4a","#984ea3","#ff7f00"]

# Generate Fibonacci numbers
fibs = [1, 1]
for _ in range(8):
    fibs.append(fibs[-1] + fibs[-2])

# Draw squares with Fibonacci side lengths, rotating to form a spiral
turns = [90, 90, 90, 90]  # repeat
turn_idx = 0
for i, n in enumerate(fibs):
    t.color(colors[i % len(colors)])
    for _ in range(4):
        t.forward(n * 5)   # scale up for visibility
        t.right(90)
    t.right(turns[turn_idx % 4])
    turn_idx += 1

turtle.done()
