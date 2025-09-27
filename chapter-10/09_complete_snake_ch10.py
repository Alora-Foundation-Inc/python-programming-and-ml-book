import turtle, random, time

# Screen
screen = turtle.Screen(); screen.title("Snake — Chapter 10 Complete")
screen.bgcolor("black"); screen.setup(600,600); screen.tracer(0)

# Head
head = turtle.Turtle(); head.speed(0); head.shape("square"); head.color("green"); head.penup(); head.goto(0,0); head.direction="stop"

# Food
food = turtle.Turtle(); food.speed(0); food.shape("circle"); food.color("red"); food.penup()

# Body list
segments = []

# Score
score = 0
high_score = 0
delay = 0.1

# Score pen
score_pen = turtle.Turtle(); score_pen.speed(0); score_pen.color("white"); score_pen.penup(); score_pen.hideturtle(); score_pen.goto(0,260)

def update_score():
    score_pen.clear()
    score_pen.write(f"Score: {score}  High Score: {high_score}  Length: {1+len(segments)}",
                    align="center", font=("Arial", 16, "bold"))

def place_food():
    food.goto(random.randint(-14,14)*20, random.randint(-12,12)*20)

def add_segment():
    s=turtle.Turtle(); s.shape("square"); s.color("lightgreen"); s.speed(0); s.penup(); segments.append(s)

def move():
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())
    if head.direction=="up": head.sety(head.ycor()+20)
    elif head.direction=="down": head.sety(head.ycor()-20)
    elif head.direction=="left": head.setx(head.xcor()-20)
    elif head.direction=="right": head.setx(head.xcor()+20)

def go_up():    (head.direction!="down") and setattr(head,"direction","up")
def go_down():  (head.direction!="up") and setattr(head,"direction","down")
def go_left():  (head.direction!="right") and setattr(head,"direction","left")
def go_right(): (head.direction!="left") and setattr(head,"direction","right")

for k,fn in [("Up",go_up),("Down",go_down),("Left",go_left),("Right",go_right)]: screen.onkey(fn, k)
screen.listen()

def reset_game():
    global score, delay, high_score
    print("Game Over! Final score:", score)
    for seg in segments:
        seg.goto(1000,1000)
    segments.clear()
    head.goto(0,0); head.direction="stop"
    if score > high_score: high_score = score
    score = 0; delay = 0.1
    place_food(); update_score()

place_food(); update_score()
print("Arrows to move. Eat the food, grow, and watch your score! (Resets if you hit a wall.)")

while True:
    # boundary considers score area at top (y=240 acts as top wall)
    if head.xcor()>290 or head.xcor()< -290 or head.ycor()>240 or head.ycor()<-290:
        reset_game()

    move()

    if head.distance(food) < 20:
        score += 10
        delay = max(0.05, delay - 0.001)
        add_segment(); place_food(); update_score()

    screen.update(); time.sleep(delay)
