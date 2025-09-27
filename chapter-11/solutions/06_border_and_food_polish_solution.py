import turtle, time, random

screen = turtle.Screen(); screen.setup(600,600); screen.bgcolor("black"); screen.tracer(0)

# draw border with stamps
b = turtle.Turtle(); b.hideturtle(); b.shape("square"); b.color("white"); b.penup()
for x in range(-290, 300, 20):
    b.goto(x, 290); b.stamp()
    b.goto(x,-290); b.stamp()
for y in range(-290, 300, 20):
    b.goto( 290, y); b.stamp()
    b.goto(-290, y); b.stamp()

food = turtle.Turtle(); food.penup()

def place_food():
    if random.random() < 0.1:
        food.shape("triangle"); food.color("gold")
    else:
        food.shape("circle"); food.color("red")
    food.goto(random.randint(-14,14)*20, random.randint(-14,14)*20)
    # flash a few times
    for _ in range(3):
        food.color("yellow"); screen.update(); time.sleep(0.1)
        food.color("gold" if food.shape()[0]=="triangle" else "red"); screen.update(); time.sleep(0.1)

place_food()
screen.exitonclick()
