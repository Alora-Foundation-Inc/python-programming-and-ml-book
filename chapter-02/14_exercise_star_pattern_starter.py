# Star Pattern — Starter
# Hint: A 5-point star uses a 144° turn each step.
# Try color lists, pensize, and movement to create a constellation.

import turtle

t = turtle.Turtle()
t.speed(7); t.pensize(2)

points = 5
size = 120
turn = 144  # 5-point star step angle

for i in range(points):
    t.forward(size)
    t.right(turn)

turtle.done()
