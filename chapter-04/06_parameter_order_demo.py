# Demonstrates that order matters for positional arguments.
# Correct: draw_polygon(3, 80, "red")
# Incorrect: draw_polygon("red", 3, 80)  # would fail

import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(6)

def draw_polygon(sides, size, color):
    my_turtle.color(color)
    angle = 360 / sides
    for _ in range(sides):
        my_turtle.forward(size)
        my_turtle.right(angle)

draw_polygon(4, 70, "purple")  # OK
# draw_polygon("purple", 4, 70)  # DON'T DO THIS

turtle.done()
