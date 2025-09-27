import turtle
t = turtle.Turtle()
t.speed(8)

for i in range(20):
    if i % 3 == 0:
        # Skip this iteration
        continue
    t.forward(50)
    t.right(18)  # 360/20

turtle.done()
