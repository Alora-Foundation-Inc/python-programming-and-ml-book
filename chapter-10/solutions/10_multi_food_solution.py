import turtle, random, time

screen = turtle.Screen(); screen.setup(600,600); screen.bgcolor("black"); screen.tracer(0)

head = turtle.Turtle(); head.shape("square"); head.color("green"); head.penup(); head.direction="right"

colors = ["red","yellow","blue","purple","orange"]
foods = []
score = 0

def make_food():
    t = turtle.Turtle(); t.shape("circle"); t.color(random.choice(colors)); t.penup()
    t.goto(random.randint(-14,14)*20, random.randint(-12,12)*20)
    return t

for _ in range(5):
    foods.append(make_food())

def move_head():
    if head.direction=="up": head.sety(head.ycor()+20)
    elif head.direction=="down": head.sety(head.ycor()-20)
    elif head.direction=="left": head.setx(head.xcor()-20)
    elif head.direction=="right": head.setx(head.xcor()+20)

screen.onkey(lambda: (head.direction!="down" and setattr(head,"direction","up")), "Up")
screen.onkey(lambda: (head.direction!="up" and setattr(head,"direction","down")), "Down")
screen.onkey(lambda: (head.direction!="right" and setattr(head,"direction","left")), "Left")
screen.onkey(lambda: (head.direction!="left" and setattr(head,"direction","right")), "Right")
screen.listen()

frames=0
while frames<600:
    move_head()
    for f in foods:
        if head.distance(f) < 20:
            score += 10
            f.goto(random.randint(-14,14)*20, random.randint(-12,12)*20)
            print("Score:", score)
    screen.update(); time.sleep(0.1); frames+=1

print("Final Score:", score)
screen.exitonclick()
