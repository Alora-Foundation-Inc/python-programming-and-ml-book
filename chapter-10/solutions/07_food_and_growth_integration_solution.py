import turtle, random, time

screen = turtle.Screen(); screen.setup(600,600); screen.bgcolor("black"); screen.tracer(0)

head = turtle.Turtle(); head.shape("square"); head.color("green"); head.penup(); head.direction="right"
food = turtle.Turtle(); food.shape("circle"); food.color("red"); food.penup()

segments = []
score = 0

def place_food():
    food.goto(random.randint(-14,14)*20, random.randint(-14,14)*20)

def add_segment():
    s=turtle.Turtle(); s.shape("square"); s.color("lightgreen"); s.speed(0); s.penup(); segments.append(s)

def move():
    for i in range(len(segments)-1,0,-1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())
    if head.direction=="up": head.sety(head.ycor()+20)
    elif head.direction=="down": head.sety(head.ycor()-20)
    elif head.direction=="left": head.setx(head.xcor()-20)
    elif head.direction=="right": head.setx(head.xcor()+20)

def up():    head.direction="up"    if head.direction!="down" else None
def down():  head.direction="down"  if head.direction!="up" else None
def left():  head.direction="left"  if head.direction!="right" else None
def right(): head.direction="right" if head.direction!="left" else None
screen.onkey(lambda: (head.direction!="down" and setattr(head,"direction","up")), "Up")
screen.onkey(lambda: (head.direction!="up" and setattr(head,"direction","down")), "Down")
screen.onkey(lambda: (head.direction!="right" and setattr(head,"direction","left")), "Left")
screen.onkey(lambda: (head.direction!="left" and setattr(head,"direction","right")), "Right")
screen.listen()

place_food()
frames=0
while frames<400:
    move()
    if head.distance(food) < 20:
        score += 10
        add_segment()
        place_food()
        print("Score:", score)
    screen.update(); time.sleep(0.12); frames += 1

print("Final score:", score)
screen.exitonclick()
