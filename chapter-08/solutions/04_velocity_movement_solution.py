import turtle, time

screen = turtle.Screen(); screen.setup(600, 400); screen.tracer(0)
player = turtle.Turtle(); player.shape("circle"); player.color("green"); player.penup()

xv = 0.0; yv = 0.0
accel = 0.5
friction = 0.95

keys = {}
def press(k): keys[k]=True
def release(k): keys[k]=False
for k in ["Up","Down","Left","Right","space"]:
    keys[k]=False
    screen.onkeypress(lambda kk=k: press(kk), k)
    screen.onkeyrelease(lambda kk=k: release(kk), k)
screen.listen()

while True:
    if keys.get("Up", False):    yv += accel
    if keys.get("Down", False):  yv -= accel
    if keys.get("Left", False):  xv -= accel
    if keys.get("Right", False): xv += accel
    if keys.get("space", False): xv *= 1.05; yv *= 1.05  # tiny boost

    xv *= friction; yv *= friction

    nx, ny = player.xcor()+xv, player.ycor()+yv
    if -280 < nx < 280: player.setx(nx)
    if -180 < ny < 180: player.sety(ny)

    screen.update(); time.sleep(0.02)
