import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

spokes = 12
for s in range(spokes):
    t.color(colors[s % len(colors)])
    # draw a short motif (little V)
    for _ in range(2):
        t.forward(80)
        t.right(60)
        t.backward(80)
        t.left(120)
    t.right(360 / spokes)

turtle.done()
