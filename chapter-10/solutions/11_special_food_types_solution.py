import turtle, random, time

screen = turtle.Screen(); screen.setup(600,600); screen.bgcolor("black"); screen.tracer(0)

head = turtle.Turtle(); head.shape("square"); head.color("green"); head.penup(); head.direction="right"
segments = []
score = 0

def add_segments(n):
    for _ in range(n):
        s=turtle.Turtle(); s.shape("square"); s.color("lightgreen"); s.speed(0); s.penup(); segments.append(s)

foods = []
# Red circle: +10, +1
r = turtle.Turtle(); r.shape("circle"); r.color("red"); r.penup(); foods.append(("red", r, 10, 1))
# Blue square: +20, +2
b = turtle.Turtle(); b.shape("square"); b.color("blue"); b.penup(); foods.append(("blue", b, 20, 2))
# Yellow triangle: +50, +0
y = turtle.Turtle(); y.shape("triangle"); y.color("yellow"); y.penup(); foods.append(("yellow", y, 50, 0))

for _, t, _, _ in foods:
    t.goto(random.randint(-14,14)*20, random.randint(-12,12)*20)

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

def follow():
    for i in range(len(segments)-1,0,-1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

while True:
    move_head(); follow()
    for name, t, points, grow in foods:
        if head.distance(t) < 20:
            score += points; add_segments(grow)
            t.goto(random.randint(-14,14)*20, random.randint(-12,12)*20)
            print(f"Ate {name}! +{points} points, +{grow} segments. Score:", score)
    screen.update(); time.sleep(0.1)
