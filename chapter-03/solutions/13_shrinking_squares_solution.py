# Solution: Shrinking Squares (decreasing size + color cycle)
import turtle

t = turtle.Turtle()
t.speed(9)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

size = 140
i = 0
while size >= 10:
    t.color(colors[i % len(colors)])
    for _ in range(4):
        t.forward(size)
        t.right(90)
    size -= 10
    i += 1
    t.penup(); t.forward(10); t.right(12); t.pendown()

turtle.done()
