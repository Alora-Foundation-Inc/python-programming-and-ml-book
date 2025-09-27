# Returning values: calculate the polygon turn angle and use it.

import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(6)

def calculate_polygon_angle(sides):
    """Return the turn angle for a regular polygon."""
    return 360 / sides

def draw_polygon(sides, size):
    angle = calculate_polygon_angle(sides)
    for _ in range(sides):
        my_turtle.forward(size)
        my_turtle.right(angle)

draw_polygon(3, 80)
my_turtle.penup(); my_turtle.goto(120, 0); my_turtle.pendown()
draw_polygon(6, 60)

turtle.done()
