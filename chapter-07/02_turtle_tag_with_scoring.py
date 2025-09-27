import turtle, random

screen = turtle.Screen()
screen.setup(400, 400)

player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()

target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()

score = 0

def new_target():
    target.goto(random.randint(-150,150), random.randint(-150,150))

def check_collision():
    global score
    if player.distance(target) < 25:
        score += 1
        print("Score:", score)
        new_target()

def move_up():    player.sety(player.ycor() + 20); check_collision()
def move_down():  player.sety(player.ycor() - 20); check_collision()
def move_left():  player.setx(player.xcor() - 20); check_collision()
def move_right(): player.setx(player.xcor() + 20); check_collision()

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.listen()

new_target()
print("Use arrow keys. Touch red circle to score!")

screen.exitonclick()
