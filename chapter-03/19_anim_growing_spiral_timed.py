import turtle
import time

t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

distance = 1
for i in range(100):
    if i % 10 == 0:
        t.color(colors[(i // 10) % len(colors)])
    t.forward(distance)
    t.right(91)
    distance += 1
    time.sleep(0.05)

turtle.done()
