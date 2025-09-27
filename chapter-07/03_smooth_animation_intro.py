import turtle, time

screen = turtle.Screen()
screen.setup(400, 300)
screen.tracer(0)   # manual updates

ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()

ball_speed = 2

while True:
    ball.setx(ball.xcor() + ball_speed)  # small step
    screen.update()                      # draw frame
    time.sleep(0.02)                     # control speed
    if ball.xcor() > 180:
        break

screen.exitonclick()
