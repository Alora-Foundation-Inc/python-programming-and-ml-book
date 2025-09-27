# TODO: make the ball bounce off all four walls (left/right/top/bottom)
import turtle, time

screen = turtle.Screen()
screen.setup(400, 400)
screen.tracer(0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()

# Add your dx, dy speeds here (e.g., dx = 3; dy = 2)

while True:
    # Move: ball.setx(ball.xcor() + dx); ball.sety(ball.ycor() + dy)
    # If hits any wall, flip that direction (dx or dy = -dx / -dy)
    screen.update()
    time.sleep(0.02)
