import turtle, time

screen = turtle.Screen(); screen.setup(800,600); screen.bgcolor("black"); screen.tracer(0)

p1 = turtle.Turtle(); p1.shape("square"); p1.color("red");  p1.penup(); p1.goto(-100,0); p1.direction="right"
p2 = turtle.Turtle(); p2.shape("square"); p2.color("blue"); p2.penup(); p2.goto( 100,0); p2.direction="left"

food = turtle.Turtle(); food.shape("circle"); food.color("yellow"); food.penup(); food.goto(0,100)

score1 = 0; score2 = 0

def move(t):
    if t.direction=="up": t.sety(t.ycor()+20)
    elif t.direction=="down": t.sety(t.ycor()-20)
    elif t.direction=="left": t.setx(t.xcor()-20)
    elif t.direction=="right": t.setx(t.xcor()+20)

def w(): (p1.direction!="down") and setattr(p1,"direction","up")
def s(): (p1.direction!="up") and setattr(p1,"direction","down")
def a(): (p1.direction!="right") and setattr(p1,"direction","left")
def d(): (p1.direction!="left") and setattr(p1,"direction","right")

def up():    (p2.direction!="down") and setattr(p2,"direction","up")
def down():  (p2.direction!="up") and setattr(p2,"direction","down")
def left():  (p2.direction!="right") and setattr(p2,"direction","left")
def right(): (p2.direction!="left") and setattr(p2,"direction","right")

for k,fn in [("w",w),("s",s),("a",a),("d",d),("Up",up),("Down",down),("Left",left),("Right",right)]: screen.onkey(fn,k)
screen.listen()

while True:
    move(p1); move(p2)
    if p1.distance(food) < 20:
        score1 += 1; food.goto(0,-100 if food.ycor()>0 else 100); print("P1 score:", score1)
    if p2.distance(food) < 20:
        score2 += 1; food.goto(0,-100 if food.ycor()>0 else 100); print("P2 score:", score2)
    screen.update(); time.sleep(0.1)
