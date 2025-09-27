import turtle, random, time

screen = turtle.Screen(); screen.setup(600,600); screen.bgcolor("black"); screen.tracer(0)

head = turtle.Turtle(); head.shape("square"); head.color("green"); head.penup(); head.direction="right"
food = turtle.Turtle(); food.shape("circle"); food.color("red"); food.penup()

segments = []
score = 0
high_score = 0
delay = 0.12

score_pen = turtle.Turtle()
score_pen.speed(0); score_pen.color("white"); score_pen.penup(); score_pen.hideturtle()
score_pen.goto(0, 260)

def update_score():
    score_pen.clear()
    score_pen.write(f"Score: {score}  High Score: {high_score}  Length: {1+len(segments)}",
                    align="center", font=("Arial", 16, "bold"))

def place_food():
    food.goto(random.randint(-14,14)*20, random.randint(-12,12)*20)  # leave room for score text

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

screen.onkey(lambda: (head.direction!="down" and setattr(head,"direction","up")), "Up")
screen.onkey(lambda: (head.direction!="up" and setattr(head,"direction","down")), "Down")
screen.onkey(lambda: (head.direction!="right" and setattr(head,"direction","left")), "Left")
screen.onkey(lambda: (head.direction!="left" and setattr(head,"direction","right")), "Right")
screen.listen()

place_food(); update_score()
frames=0
while frames<300:
    move()
    if head.distance(food) < 20:
        score += 10
        if score > high_score: high_score = score
        delay = max(0.05, delay - 0.002)
        add_segment(); place_food(); update_score()
    screen.update(); time.sleep(delay); frames += 1

print("Done. Final Score:", score)
screen.exitonclick()
