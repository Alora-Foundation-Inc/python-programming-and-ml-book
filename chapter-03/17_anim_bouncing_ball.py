import turtle
import time

screen = turtle.Screen()
screen.tracer(0)          # manual screen updates for smooth animation

ball = turtle.Turtle()
ball.hideturtle()
ball.penup()

# initial state
x, y = 0, 0
dx, dy = 3, 4
radius = 12

while True:
    # clear previous frame
    ball.clear()

    # update position
    x += dx
    y += dy

    # bounce on borders
    if x > 300 - radius or x < -300 + radius:
        dx = -dx
    if y > 200 - radius or y < -200 + radius:
        dy = -dy

    # draw the ball (a dot)
    ball.goto(x, y)
    ball.dot(radius * 2)

    screen.update()
    time.sleep(0.02)
