import turtle

t = turtle.Turtle()
t.speed(7)

size = 20
colors = ["red", "orange", "yellow", "green", "blue"]

for color in colors:
    t.color(color)

    # draw one square
    for side in range(4):
        t.forward(size)
        t.right(90)

    # prepare next square: bigger and re-centered
    size = size + 20
    t.penup()
    t.goto(-size/2, -size/2)
    t.pendown()

turtle.done()
