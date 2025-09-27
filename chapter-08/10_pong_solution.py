import turtle, time

screen = turtle.Screen(); screen.setup(800, 500); screen.bgcolor("black"); screen.title("Simple Pong")
screen.tracer(0)

leftp = turtle.Turtle(); leftp.shape("square"); leftp.color("white"); leftp.shapesize(5,1); leftp.penup(); leftp.goto(-360,0)
rightp = turtle.Turtle(); rightp.shape("square"); rightp.color("white"); rightp.shapesize(5,1); rightp.penup(); rightp.goto(360,0)

ball = turtle.Turtle(); ball.shape("square"); ball.color("white"); ball.penup(); ball.goto(0,0)
ball_dx, ball_dy = 4, 3

keys = {}
def press(k): keys[k]=True
def release(k): keys[k]=False
for k in ["w","s","Up","Down"]:
    keys[k]=False
    screen.onkeypress(lambda kk=k: press(kk), k)
    screen.onkeyrelease(lambda kk=k: release(kk), k)
screen.listen()

def clamp_paddle(p):
    if p.ycor() > 200: p.sety(200)
    if p.ycor() < -200: p.sety(-200)

while True:
    # Paddle movement
    if keys.get("w", False): leftp.sety(leftp.ycor()+6); clamp_paddle(leftp)
    if keys.get("s", False): leftp.sety(leftp.ycor()-6); clamp_paddle(leftp)
    if keys.get("Up", False): rightp.sety(rightp.ycor()+6); clamp_paddle(rightp)
    if keys.get("Down", False): rightp.sety(rightp.ycor()-6); clamp_paddle(rightp)

    # Ball movement
    ball.setx(ball.xcor()+ball_dx); ball.sety(ball.ycor()+ball_dy)

    # Wall bounce
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball_dy = -ball_dy

    # Paddle bounce (simple distance checks)
    if ball.xcor() < -340 and leftp.distance(ball) < 60:
        ball_dx = abs(ball_dx)
    if ball.xcor() > 340 and rightp.distance(ball) < 60:
        ball_dx = -abs(ball_dx)

    # Out of bounds -> reset
    if ball.xcor() < -390 or ball.xcor() > 390:
        ball.goto(0,0); ball_dx = -ball_dx

    screen.update(); time.sleep(0.02)
