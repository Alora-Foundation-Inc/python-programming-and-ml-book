import turtle
import time

screen = turtle.Screen()
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.pensize(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
spokes = 18
angle = 0
size = 40

while angle < 360:
    t.clear()
    t.penup(); t.goto(0, 0); t.pendown()
    for s in range(spokes):
        t.color(colors[(s + int(angle/10)) % len(colors)])
        t.setheading(angle + s * (360 / spokes))
        t.forward(size)
        t.right(30)
        t.forward(20)
        t.backward(20)
        t.left(30)
        t.backward(size)
    screen.update()
    time.sleep(0.05)
    angle += 5
    size = size + 0.2

turtle.done()
