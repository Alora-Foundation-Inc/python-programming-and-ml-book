# Dodge falling red squares; survive the timer!
import turtle, random, time

screen = turtle.Screen()
screen.setup(600, 400)
screen.bgcolor("skyblue")
screen.tracer(0)

player = turtle.Turtle(); player.shape("turtle"); player.color("green"); player.penup()
player.goto(0, -150)

def left_(): player.setx(max(player.xcor()-20, -280))
def right_(): player.setx(min(player.xcor()+20,  280))

screen.onkey(left_, "Left"); screen.onkey(right_, "Right"); screen.listen()

obstacles = []  # list of obstacle turtles

# TODO in loop:
# - occasionally spawn a red square at top edge
# - move each obstacle down each frame
# - remove obstacles that pass the bottom
# - if player.distance(obstacle) < threshold -> game over
# - stop after ~30 seconds and print win/lose
screen.exitonclick()
