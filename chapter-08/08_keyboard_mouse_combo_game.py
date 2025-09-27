import turtle, time

screen = turtle.Screen(); screen.setup(600, 400); screen.bgcolor("navy"); screen.tracer(0)

player = turtle.Turtle(); player.shape("triangle"); player.color("white"); player.penup()
target = turtle.Turtle(); target.shape("circle"); target.color("red"); target.penup(); target.goto(100,100)

score = 0; t = 0
keys = {}
def press(k): keys[k]=True
def release(k): keys[k]=False
for k in ["Up","Down","Left","Right"]:
    keys[k]=False
    screen.onkeypress(lambda kk=k: press(kk), k)
    screen.onkeyrelease(lambda kk=k: release(kk), k)

def move_target(x,y): target.goto(x,y)
screen.onscreenclick(move_target); screen.listen()

while t < 600:
    if keys.get("Up", False): player.sety(player.ycor()+3)
    if keys.get("Down", False): player.sety(player.ycor()-3)
    if keys.get("Left", False): player.setx(player.xcor()-3)
    if keys.get("Right", False): player.setx(player.xcor()+3)

    if player.distance(target) < 25:
        score += 1
        target.color("yellow"); screen.update(); time.sleep(0.1); target.color("red")
        print("Score:", score)

    screen.update(); time.sleep(0.02); t += 1

print("Final Score:", score)
screen.mainloop()
