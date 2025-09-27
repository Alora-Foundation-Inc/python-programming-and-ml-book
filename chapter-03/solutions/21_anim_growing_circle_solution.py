# Solution: Animated Growing Circle (radius 10..100)
import turtle, time

screen = turtle.Screen()
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.pensize(2)
t.color("blue")

for r in range(10, 105, 5):
    t.clear()
    t.penup(); t.goto(0, -r); t.pendown()  # center the circle visually
    t.circle(r)
    screen.update()
    time.sleep(0.05)

turtle.done()
