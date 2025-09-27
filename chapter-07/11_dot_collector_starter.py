# Collect yellow dots by touching them with your player.
import turtle, random, time

screen = turtle.Screen()
screen.setup(600, 400)
screen.bgcolor("black")
screen.tracer(0)

player = turtle.Turtle(); player.shape("triangle"); player.color("cyan"); player.penup()

dots = []   # list of dot turtles
score = 0

def create_dot():
    d = turtle.Turtle(); d.shape("circle"); d.color("yellow"); d.penup()
    d.goto(random.randint(-280, 280), random.randint(-180, 180))
    dots.append(d)

# spawn a few to start
for _ in range(5): create_dot()

def up(): player.sety(player.ycor()+20)
def down(): player.sety(player.ycor()-20)
def left_(): player.setx(player.xcor()-20)
def right_(): player.setx(player.xcor()+20)

screen.onkey(up,"Up"); screen.onkey(down,"Down"); screen.onkey(left_,"Left"); screen.onkey(right_,"Right")
screen.listen()

# TODO: make a game loop for ~30 seconds:
# - check collisions: if player.distance(dot) < 20 -> hide & remove & +score
# - update screen and sleep a tiny bit
# - print final score at the end
screen.exitonclick()
