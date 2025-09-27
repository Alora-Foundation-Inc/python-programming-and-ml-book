import turtle, time, random

screen = turtle.Screen(); screen.setup(600,600); screen.bgcolor("black"); screen.tracer(0)

head = turtle.Turtle(); head.shape("square"); head.color("lime"); head.penup(); head.direction="right"
segments = []
score = 0
delay = 0.12
power = {"name": None, "timer": 0}

food = turtle.Turtle(); food.shape("circle"); food.color("red"); food.penup(); food.goto(0,100)
orb  = turtle.Turtle();  orb.shape("circle");  orb.color("cyan");  orb.penup();  orb.goto(200,0)   # slow time
star = turtle.Turtle(); star.shape("triangle"); star.color("gold"); star.penup(); star.goto(-200,0) # double points

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

def tick_power():
    if power["timer"]>0:
        power["timer"] -= 1
        if power["timer"]==0:
            power["name"]=None
            print("Power expired")

running=True; frame=0
while running:
    move()
    if head.distance(food)<20:
        add_segment()
        score += (20 if power["name"]=="double" else 10)
        food.goto(random.randint(-14,14)*20, random.randint(-14,14)*20)
        print("Score:", score)
    if head.distance(orb)<20:
        power["name"]="slow"; power["timer"]=100; orb.goto(1000,1000); print("Slow time!")
    if head.distance(star)<20:
        power["name"]="double"; power["timer"]=160; star.goto(1000,1000); print("Double points!")

    tick_power()
    if head.xcor()>280 or head.xcor()< -280 or head.ycor()>280 or head.ycor()< -280:
        running=False
    screen.update(); time.sleep(0.2 if power["name"]=="slow" else 0.1)
    frame += 1

print("Game over. Final score:", score)
screen.exitonclick()
