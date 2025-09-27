import turtle, random, time

screen = turtle.Screen(); screen.setup(600,600); screen.bgcolor("black"); screen.tracer(0)

head = turtle.Turtle(); head.shape("square"); head.color("lime"); head.penup(); head.direction="right"
segments = []
obstacles = []

def block(x,y):
    t=turtle.Turtle(); t.shape("square"); t.color("white"); t.penup(); t.goto(x,y); obstacles.append(t)

# random obstacles
for _ in range(20):
    block(random.randint(-14,14)*20, random.randint(-14,14)*20)

food = turtle.Turtle(); food.shape("circle"); food.color("red"); food.penup()

def safe_food():
    while True:
        x,y = random.randint(-14,14)*20, random.randint(-14,14)*20
        if all(abs(x-o.xcor())>1 or abs(y-o.ycor())>1 for o in obstacles):
            return x,y

food.goto(safe_food())

def add_segment():
    s=turtle.Turtle(); s.shape("square"); s.color("lightgreen"); s.penup(); segments.append(s)

def move():
    for i in range(len(segments)-1,0,-1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())
    if head.direction=="up": head.sety(head.ycor()+20)
    elif head.direction=="down": head.sety(head.ycor()-20)
    elif head.direction=="left": head.setx(head.xcor()-20)
    elif head.direction=="right": head.setx(head.xcor()+20)

screen.onkey(lambda: (head.direction!="down" and setattr(head,"direction","up")), "Up")
screen.onkey(lambda: (head.direction!="up" and setattr(head,"direction","down")), "Down")
screen.onkey(lambda: (head.direction!="right" and setattr(head,"direction","left")), "Left")
screen.onkey(lambda: (head.direction!="left" and setattr(head,"direction","right")), "Right")
screen.listen()

running=True
while running:
    move()
    if head.distance(food)<20:
        add_segment(); food.goto(safe_food())
    if head.xcor()>280 or head.xcor()< -280 or head.ycor()>280 or head.ycor()< -280:
        running=False
    if any(head.distance(o)<15 for o in obstacles):
        running=False
    screen.update(); time.sleep(0.1)

print("Hit wall or obstacle — game over")
screen.exitonclick()
