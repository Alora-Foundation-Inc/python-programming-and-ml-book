import turtle, time

screen = turtle.Screen(); screen.setup(400, 400); screen.tracer(0)
player = turtle.Turtle(); player.shape("triangle"); player.color("red"); player.penup()

keys = {}
def key_press(k): keys[k] = True
def key_release(k): keys[k] = False

for k in ["Up", "Down", "Left", "Right", "space"]:
    keys[k] = False
    screen.onkeypress(lambda kk=k: key_press(kk), k)
    screen.onkeyrelease(lambda kk=k: key_release(kk), k)

screen.listen()

while True:
    if keys.get("Up", False): player.sety(player.ycor()+2)
    if keys.get("Down", False): player.sety(player.ycor()-2)
    if keys.get("Left", False): player.setx(player.xcor()-2)
    if keys.get("Right", False): player.setx(player.xcor()+2)
    player.color("yellow" if keys.get("space", False) else "red")
    screen.update(); time.sleep(0.02)
