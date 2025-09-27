import turtle, random, time

screen = turtle.Screen(); screen.setup(600, 400); screen.tracer(0)

score = 0
targets = []

def hit_target(x, y):
    global score
    score += 1
    print("Hit! Score:", score)

def make_target():
    t = turtle.Turtle(); t.shape("circle"); t.color("red"); t.penup()
    t.goto(random.randint(-280,280), random.randint(-180,180))
    t.onclick(hit_target); targets.append(t)

frames = 0
while frames < 600:  # ~30s
    if frames % 30 == 0:  # spawn every 1.5s
        make_target()
    # optional: remove oldest if too many
    if len(targets) > 8:
        old = targets.pop(0); old.hideturtle()
    screen.update(); time.sleep(0.05); frames += 1

print("Final Score:", score)
screen.exitonclick()
