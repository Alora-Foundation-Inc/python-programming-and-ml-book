import turtle, time, random

screen = turtle.Screen(); screen.setup(600, 400); screen.bgcolor("black"); screen.tracer(0)

# 1) Ship controlled with arrow keys
ship = turtle.Turtle(); ship.shape("triangle"); ship.color("cyan"); ship.penup()

# 2) Asteroids that move across
asteroids = []

# 3) Collision ends the game
alive = True; frames = 0

# Controls
keys = {}
def press(k): keys[k]=True
def release(k): keys[k]=False
for k in ["Up","Down","Left","Right"]:
    keys[k]=False
    screen.onkeypress(lambda kk=k: press(kk), k)
    screen.onkeyrelease(lambda kk=k: release(kk), k)
screen.listen()

print("Survive as long as you can! (Starter file)")

while alive:
    # TODO: move ship, spawn/move asteroids, detect collisions, track time
    screen.update(); time.sleep(0.03); frames += 1
screen.exitonclick()
