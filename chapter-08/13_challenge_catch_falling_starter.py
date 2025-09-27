import turtle, time, random

screen = turtle.Screen(); screen.setup(600, 400); screen.tracer(0)

player = turtle.Turtle(); player.shape("square"); player.color("white"); player.penup(); player.goto(0,-160)
falling = []; score = 0; misses = 0

keys = {}
def press(k): keys[k]=True
def release(k): keys[k]=False
for k in ["Left","Right"]:
    keys[k]=False
    screen.onkeypress(lambda kk=k: press(kk), k)
    screen.onkeyrelease(lambda kk=k: release(kk), k)
screen.listen()

print("Catch the falling objects! (Starter file)")

while True:
    # TODO: spawn objects, move them down, move player, detect catches/misses, end after N misses
    screen.update(); time.sleep(0.05)
