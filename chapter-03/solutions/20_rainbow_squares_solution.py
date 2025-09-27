# Solution: Rainbow Squares (nested loops, 7 colors)
import turtle

t = turtle.Turtle()
t.speed(8)
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

size = 40
for c in rainbow:
    t.color(c)
    for _ in range(4):
        t.forward(size)
        t.right(90)
    size += 20
    t.penup(); t.goto(-size/2, -size/2); t.pendown()

turtle.done()
