import turtle, time

screen = turtle.Screen()
screen.setup(400, 300)
screen.tracer(0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()

dx = 3

while True:
    ball.setx(ball.xcor() + dx)
    if ball.xcor() > 180 or ball.xcor() < -180:
        dx = -dx  # bounce
    screen.update()
    time.sleep(0.02)
