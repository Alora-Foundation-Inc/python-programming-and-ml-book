import turtle
import time

screen = turtle.Screen()
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.color("green")
t.pensize(3)

angle = 0
while angle < 360:
    t.clear()
    t.setheading(angle)
    t.penup(); t.goto(0, 0); t.pendown()
    t.forward(120)
    screen.update()
    time.sleep(0.05)
    angle += 5

turtle.done()
