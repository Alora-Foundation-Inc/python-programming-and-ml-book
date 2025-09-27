import turtle

t = turtle.Turtle()
t.speed(7); t.pensize(3)

sides = 7            # try 3..10
side_length = 80
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

angle = 360 / sides

for i in range(sides):
    t.color(colors[i % len(colors)])  # cycle colors
    t.forward(side_length)
    t.right(angle)

turtle.done()
