# Rainbow Polygon — Starter
# TODO:
# 1) Make a list of at least 5 colors.
# 2) Choose the number of sides (3..10) and compute angle = 360 / sides.
# 3) Use a for loop to draw the polygon, changing color each side.

import turtle

t = turtle.Turtle()
t.speed(6); t.pensize(3)

# Your variables here:
sides = 6
side_length = 80
colors = ["red", "orange", "yellow", "green", "blue"]

angle = 360 / sides

for i in range(sides):
    t.color(colors[i % len(colors)])
    t.forward(side_length)
    t.right(angle)

turtle.done()
