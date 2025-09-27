import turtle, time

screen = turtle.Screen()
screen.setup(400, 400)
screen.tracer(0)

ball = turtle.Turtle(); ball.shape("circle"); ball.color("green"); ball.penup()

dx, dy = 3, 2

while True:
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    if ball.xcor() > 190 or ball.xcor() < -190: dx = -dx
    if ball.ycor() > 190 or ball.ycor() < -190: dy = -dy

    screen.update(); time.sleep(0.02)
