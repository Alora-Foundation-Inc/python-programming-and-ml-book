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

obstacles = []
frames = 0
alive = True

def spawn_obstacle():
    o = turtle.Turtle(); o.shape("square"); o.color("red"); o.penup()
    o.goto(random.randint(-280, 280), 190)
    obstacles.append(o)

while frames < 600 and alive:   # ~30s
    if frames % 20 == 0:  # every ~1s
        spawn_obstacle()

    for o in list(obstacles):
        o.sety(o.ycor() - 6)  # fall speed
        if o.ycor() < -200:
            o.hideturtle(); obstacles.remove(o)
        elif player.distance(o) < 25:
            alive = False
            break

    screen.update(); time.sleep(0.05); frames += 1

print("You survived!" if alive else "Hit by an obstacle!")
screen.exitonclick()
