import turtle, time, random

screen = turtle.Screen()
screen.setup(600, 400)
screen.tracer(0)

player = turtle.Turtle(); player.shape("turtle"); player.color("green"); player.penup()
target = turtle.Turtle(); target.shape("circle"); target.color("red"); target.penup()

score = 0

def move_up(): player.sety(player.ycor() + 20)
def move_down(): player.sety(player.ycor() - 20)
def move_left(): player.setx(player.xcor() - 20)
def move_right(): player.setx(player.xcor() + 20)

screen.onkey(move_up, "Up"); screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left"); screen.onkey(move_right, "Right")
screen.listen()

game_time = 0
while game_time < 300:  # ~15 seconds
    if game_time % 60 == 0:
        target.goto(random.randint(-250, 250), random.randint(-150, 150))
    if player.distance(target) < 30:
        score += 1
        print("Score:", score)
        target.goto(random.randint(-250, 250), random.randint(-150, 150))
    screen.update()
    time.sleep(0.05)
    game_time += 1

print("Game Over! Final Score:", score)
screen.exitonclick()
