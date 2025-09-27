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

def new_target():
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    target.goto(x, y)

def move_up(): player.sety(player.ycor() + 20)
def move_down(): player.sety(player.ycor() - 20)

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.listen()

new_target()
print("Use Up/Down arrows to catch the red circle! (No scoring yet)")

screen.exitonclick()
