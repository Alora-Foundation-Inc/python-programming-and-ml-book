import turtle, time, math

screen = turtle.Screen(); screen.setup(400, 400); screen.tracer(0)
player = turtle.Turtle(); player.shape("triangle"); player.color("blue"); player.penup()

angle = 0
speed = 3

keys = {}
def press(k): keys[k]=True
def release(k): keys[k]=False
for k in ["Up","Left","Right"]:
    keys[k]=False
    screen.onkeypress(lambda kk=k: press(kk), k)
    screen.onkeyrelease(lambda kk=k: release(kk), k)
screen.listen()

while True:
    if keys.get("Left", False):  angle += 5
    if keys.get("Right", False): angle -= 5
    player.setheading(angle)

    if keys.get("Up", False):
        dx = speed * math.cos(math.radians(angle))
        dy = speed * math.sin(math.radians(angle))
        nx, ny = player.xcor()+dx, player.ycor()+dy
        if nx > 190: nx = -190
        if nx < -190: nx = 190
        if ny > 190: ny = -190
        if ny < -190: ny = 190
        player.goto(nx, ny)

    screen.update(); time.sleep(0.02)
