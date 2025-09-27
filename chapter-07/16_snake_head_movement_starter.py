# Move a 'snake head' continuously; change direction with keys.
import turtle, time

screen = turtle.Screen(); screen.setup(600, 400); screen.tracer(0)

head = turtle.Turtle(); head.shape("square"); head.color("lime"); head.penup()
head.setheading(0)  # start moving right
speed = 10

def up():    head.setheading(90)
def down():  head.setheading(270)
def left_(): head.setheading(180)
def right_():head.setheading(0)

screen.onkey(up,"Up"); screen.onkey(down,"Down"); screen.onkey(left_,"Left"); screen.onkey(right_,"Right"); screen.listen()

# TODO loop:
# - move forward a small step each frame (head.forward(...))
# - stop if head goes beyond walls
screen.exitonclick()
