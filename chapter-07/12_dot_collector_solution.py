import turtle, random, time

screen = turtle.Screen()
screen.setup(600, 400)
screen.bgcolor("black")
screen.tracer(0)

player = turtle.Turtle(); player.shape("triangle"); player.color("cyan"); player.penup()

dots = []
score = 0

def create_dot():
    d = turtle.Turtle(); d.shape("circle"); d.color("yellow"); d.penup()
    d.goto(random.randint(-280, 280), random.randint(-180, 180))
    dots.append(d)

for _ in range(8): create_dot()

def up(): player.sety(player.ycor()+20)
def down(): player.sety(player.ycor()-20)
def left_(): player.setx(player.xcor()-20)
def right_(): player.setx(player.xcor()+20)

screen.onkey(up,"Up"); screen.onkey(down,"Down"); screen.onkey(left_,"Left"); screen.onkey(right_,"Right")
screen.listen()

frames = 0
while frames < 600:  # ~30s at 0.05s per frame
    # collision check
    for d in list(dots):
        if player.distance(d) < 20:
            score += 1
            d.hideturtle()
            dots.remove(d)
    # win early if all collected
    if not dots:
        print("You collected all dots! Score:", score)
        break
    screen.update(); time.sleep(0.05); frames += 1

print("Final Score:", score)
screen.exitonclick()
