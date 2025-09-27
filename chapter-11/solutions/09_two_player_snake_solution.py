import turtle, time, random

screen = turtle.Screen(); screen.setup(800,600); screen.bgcolor("black"); screen.tracer(0)

p1 = turtle.Turtle(); p1.shape("square"); p1.color("red");  p1.penup(); p1.goto(-100,0); p1.direction="right"
p2 = turtle.Turtle(); p2.shape("square"); p2.color("blue"); p2.penup(); p2.goto( 100,0); p2.direction="left"

segments1, segments2 = [], []
food = turtle.Turtle(); food.shape("circle"); food.color("yellow"); food.penup(); food.goto(0,100)

def move(t, segs):
    for i in range(len(segs)-1, 0, -1): segs[i].goto(segs[i-1].xcor(), segs[i-1].ycor())
    if segs: segs[0].goto(t.xcor(), t.ycor())
    if t.direction=="up": t.sety(t.ycor()+20)
    elif t.direction=="down": t.sety(t.ycor()-20)
    elif t.direction=="left": t.setx(t.xcor()-20)
    elif t.direction=="right": t.setx(t.xcor()+20)

def grow(segs):
    s=turtle.Turtle(); s.shape("square"); s.color("gray"); s.penup(); segs.append(s)

def bind_player(t, keys):
    up,down,left,right = keys
    screen.onkey(lambda: (t.direction!="down" and setattr(t,"direction","up")), up)
    screen.onkey(lambda: (t.direction!="up" and setattr(t,"direction","down")), down)
    screen.onkey(lambda: (t.direction!="right" and setattr(t,"direction","left")), left)
    screen.onkey(lambda: (t.direction!="left" and setattr(t,"direction","right")), right)

bind_player(p1, ("w","s","a","d"))
bind_player(p2, ("Up","Down","Left","Right"))
screen.listen()

def out_of_bounds(t):
    return t.xcor()>380 or t.xcor()< -380 or t.ycor()>280 or t.ycor()< -280

running=True
while running:
    move(p1,segments1); move(p2,segments2)
    if p1.distance(food)<20: grow(segments1); food.goto(random.randint(-18,18)*20, random.randint(-13,13)*20)
    if p2.distance(food)<20: grow(segments2); food.goto(random.randint(-18,18)*20, random.randint(-13,13)*20)
    # collisions
    if out_of_bounds(p1) or out_of_bounds(p2): running=False
    for s in segments1[2:]:
        if p1.distance(s)<20 or p2.distance(s)<20: running=False
    for s in segments2[2:]:
        if p2.distance(s)<20 or p1.distance(s)<20: running=False
    screen.update(); time.sleep(0.1)

print("Game over!")
screen.exitonclick()
