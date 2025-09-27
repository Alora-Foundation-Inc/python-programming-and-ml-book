# Solution: Growing Spiral (color-cycling + increasing steps)
import turtle

t = turtle.Turtle()
t.speed(9)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

distance = 3
angle = 91
for i in range(120):
    t.color(colors[i % len(colors)])
    t.forward(distance)
    t.right(angle)
    distance += 1

turtle.done()
