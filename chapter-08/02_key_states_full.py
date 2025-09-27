import turtle, time

screen = turtle.Screen(); screen.setup(600, 400); screen.tracer(0)
player = turtle.Turtle(); player.shape("square"); player.color("blue"); player.penup()

keys_pressed = {"Up": False, "Down": False, "Left": False, "Right": False}

def up_press(): keys_pressed["Up"] = True
def up_release(): keys_pressed["Up"] = False
def down_press(): keys_pressed["Down"] = True
def down_release(): keys_pressed["Down"] = False
def left_press(): keys_pressed["Left"] = True
def left_release(): keys_pressed["Left"] = False
def right_press(): keys_pressed["Right"] = True
def right_release(): keys_pressed["Right"] = False

screen.onkeypress(up_press, "Up"); screen.onkeyrelease(up_release, "Up")
screen.onkeypress(down_press, "Down"); screen.onkeyrelease(down_release, "Down")
screen.onkeypress(left_press, "Left"); screen.onkeyrelease(left_release, "Left")
screen.onkeypress(right_press, "Right"); screen.onkeyrelease(right_release, "Right")
screen.listen()

while True:
    if keys_pressed["Up"]: player.sety(player.ycor()+3)
    if keys_pressed["Down"]: player.sety(player.ycor()-3)
    if keys_pressed["Left"]: player.setx(player.xcor()-3)
    if keys_pressed["Right"]: player.setx(player.xcor()+3)
    screen.update(); time.sleep(0.02)
