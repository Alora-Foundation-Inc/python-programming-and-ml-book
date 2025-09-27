import turtle
t = turtle.Turtle()
t.speed(7)

for color in ["red", "green", "blue"]:
    t.color(color)
    # draw one triangle
    for _ in range(3):
        t.forward(80)
        t.left(120)
    # shift to the right for the next one
    t.penup()
    t.forward(120)
    t.pendown()

turtle.done()
