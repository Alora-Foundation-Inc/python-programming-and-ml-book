import turtle, time, random

screen = turtle.Screen(); screen.setup(600, 400); screen.tracer(0)

player = turtle.Turtle(); player.shape("square"); player.color("white"); player.penup(); player.goto(0,-160)
falling = []; score = 0; misses = 0

keys = {}
def press(k): keys[k]=True
def release(k): keys[k]=False
for k in ["Left","Right"]:
    keys[k]=False
    screen.onkeypress(lambda kk=k: press(kk), k)
    screen.onkeyrelease(lambda kk=k: release(kk), k)
screen.listen()

frames = 0
running = True
def spawn():
    t = turtle.Turtle(); t.shape("circle"); t.color("gold"); t.penup()
    t.goto(random.randint(-280,280), 190); t.dy = -random.randint(3,6)
    falling.append(t)

while running:
    if keys.get("Left", False): player.setx(max(-280, player.xcor()-8))
    if keys.get("Right", False): player.setx(min( 280, player.xcor()+8))

    if frames % 20 == 0: spawn()

    for obj in list(falling):
        obj.sety(obj.ycor()+obj.dy)
        if obj.ycor() < -180:
            misses += 1; obj.hideturtle(); falling.remove(obj)
            print("Misses:", misses)
            if misses >= 5: running = False
        elif obj.distance(player) < 20:
            score += 1; obj.hideturtle(); falling.remove(obj); print("Score:", score)

    screen.update(); time.sleep(0.05); frames += 1

print("Final score:", score, "| Misses:", misses)
screen.exitonclick()
