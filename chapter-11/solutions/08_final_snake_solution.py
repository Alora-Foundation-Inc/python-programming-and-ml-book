import turtle, time, random

# ------------- Screen & Border -------------
screen = turtle.Screen(); screen.setup(600,600); screen.bgcolor("black"); screen.tracer(0); screen.title("Ultimate Snake — Chapter 11")

# Draw border
border = turtle.Turtle(); border.hideturtle(); border.shape("square"); border.color("white"); border.penup()
for x in range(-290, 300, 20):
    border.goto(x, 290); border.stamp()
    border.goto(x,-290); border.stamp()
for y in range(-290, 300, 20):
    border.goto( 290, y); border.stamp()
    border.goto(-290, y); border.stamp()

# ------------- Actors -------------
head = turtle.Turtle(); head.shape("square"); head.color("lime"); head.penup(); head.goto(0,0); head.direction = "right"
food = turtle.Turtle(); food.penup()

segments = []

# ------------- Game State -------------
score = 0
high_score = 0
level = 1
food_eaten = 0
game_over = False
paused = False
food_type = "normal"  # "normal" or "special"

# ------------- Pens -------------
score_pen = turtle.Turtle(); score_pen.hideturtle(); score_pen.color("white"); score_pen.penup(); score_pen.goto(0,260)
game_over_pen = turtle.Turtle(); game_over_pen.hideturtle(); game_over_pen.color("red"); game_over_pen.penup()

# ------------- Helpers -------------
def update_display():
    score_pen.clear()
    score_pen.write(f"Score: {score}  High: {high_score}  Level: {level}  Length: {1+len(segments)}",
                    align="center", font=("Arial", 16, "bold"))

def calculate_speed():
    base_delay = 0.12
    return max(0.05, base_delay - (level-1)*0.02)

def place_food():
    global food_type
    if random.random() < 0.10:
        food.shape("triangle"); food.color("gold"); food_type = "special"
    else:
        food.shape("circle"); food.color("red"); food_type = "normal"
    food.goto(random.randint(-14,14)*20, random.randint(-14,14)*20)
    # quick flash animation
    for _ in range(3):
        food.color("yellow"); screen.update(); time.sleep(0.08)
        food.color("gold" if food_type=="special" else "red"); screen.update(); time.sleep(0.08)

def add_segment(n=1):
    for _ in range(n):
        s = turtle.Turtle(); s.shape("square"); s.color("lightgreen"); s.speed(0); s.penup()
        segments.append(s)

def move():
    # body follow
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())
    # head step
    if head.direction=="up": head.sety(head.ycor()+20)
    elif head.direction=="down": head.sety(head.ycor()-20)
    elif head.direction=="left": head.setx(head.xcor()-20)
    elif head.direction=="right": head.setx(head.xcor()+20)

def go_up():    (not game_over and not paused and head.direction!="down") and setattr(head, "direction", "up")
def go_down():  (not game_over and not paused and head.direction!="up") and setattr(head, "direction", "down")
def go_left():  (not game_over and not paused and head.direction!="right") and setattr(head, "direction", "left")
def go_right(): (not game_over and not paused and head.direction!="left") and setattr(head, "direction", "right")

def show_game_over():
    game_over_pen.clear()
    game_over_pen.goto(0,30)
    game_over_pen.write("GAME OVER!", align="center", font=("Arial", 26, "bold"))
    game_over_pen.goto(0,-10)
    game_over_pen.write(f"Final Score: {score}   Level: {level}   Length: {1+len(segments)}", align="center", font=("Arial", 14, "normal"))
    game_over_pen.goto(0,-40)
    game_over_pen.write("Press R to Restart • Q to Quit • Space to Pause/Resume", align="center", font=("Arial", 12, "normal"))
    screen.update()

def restart_game():
    global score, level, food_eaten, game_over, paused, segments, head, high_score
    # update high score
    if score > high_score: 
        high_score = score
    # clear segments
    for seg in segments:
        seg.goto(1000,1000)
    segments.clear()
    # reset state
    score = 0; level = 1; food_eaten = 0; game_over = False; paused = False
    head.goto(0,0); head.direction = "right"
    game_over_pen.clear()
    place_food(); update_display()
    print("Restart!")

def toggle_pause():
    global paused
    if not game_over:
        paused = not paused
        print("Paused" if paused else "Resumed")

def check_food():
    global score, level, food_eaten
    if head.distance(food) < 20:
        if food_type == "special":
            score += 30; add_segment(2)
        else:
            score += 10; add_segment(1)
        food_eaten += 1
        if food_eaten % 5 == 0:
            level += 1; print("Level up! Now level", level)
        place_food(); update_display()

def check_collisions():
    global game_over, high_score
    # wall (leave room under score bar: y<=260 top boundary)
    if head.xcor()>280 or head.xcor()< -280 or head.ycor()>260 or head.ycor()< -280:
        game_over = True
    # self — skip first two body parts to avoid immediate neighbor contact
    for seg in segments[2:]:
        if head.distance(seg) < 20:
            game_over = True
            break
    if game_over:
        if score > high_score: high_score = score
        show_game_over()

# Keybinds
screen.onkey(go_up, "Up"); screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left"); screen.onkey(go_right, "Right")
screen.onkey(restart_game, "r"); screen.onkey(toggle_pause, "space")
screen.onkey(screen.bye, "q")
screen.listen()

# Initial setup
place_food(); update_display()
print("Ultimate Snake — Arrows move • R restart • Q quit • Space pause")

# Main loop
while True:
    screen.update()
    if not game_over and not paused:
        move()
        check_collisions()
        check_food()
        time.sleep(calculate_speed())
    else:
        time.sleep(0.1)
