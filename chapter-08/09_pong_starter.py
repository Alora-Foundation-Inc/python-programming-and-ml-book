import turtle, time

screen = turtle.Screen(); screen.setup(800, 500); screen.bgcolor("black"); screen.title("Simple Pong")
screen.tracer(0)

# Paddles
leftp = turtle.Turtle(); leftp.shape("square"); leftp.color("white"); leftp.shapesize(5,1); leftp.penup(); leftp.goto(-360,0)
rightp = turtle.Turtle(); rightp.shape("square"); rightp.color("white"); rightp.shapesize(5,1); rightp.penup(); rightp.goto(360,0)

# Ball
ball = turtle.Turtle(); ball.shape("square"); ball.color("white"); ball.penup(); ball.goto(0,0)
ball_dx, ball_dy = 4, 3

# Key state
keys = {}
def press(k): keys[k]=True
def release(k): keys[k]=False
for k in ["w","s","Up","Down"]:
    keys[k]=False
    screen.onkeypress(lambda kk=k: press(kk), k)
    screen.onkeyrelease(lambda kk=k: release(kk), k)
screen.listen()

print("Left: W/S  |  Right: Up/Down")
print("TODO for you: move paddles with keys, bounce ball on walls & paddles, reset when out.")

while True:
    # TODO:
    # - If keys['w']: leftp.sety(leftp.ycor()+?) (stay in bounds)
    # - If keys['s']: leftp.sety(leftp.ycor()-?)
    # - If keys['Up']: rightp.sety(...)
    # - If keys['Down']: rightp.sety(...)
    # - Move ball with ball_dx/ball_dy; bounce off top/bottom
    # - If ball near paddle & correct x, reverse ball_dx
    # - If ball goes past left/right, center it & reverse ball_dx
    screen.update(); time.sleep(0.02)
