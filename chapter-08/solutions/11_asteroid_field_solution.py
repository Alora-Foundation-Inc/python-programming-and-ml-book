import turtle, time, random

screen = turtle.Screen(); screen.setup(600, 400); screen.bgcolor("black"); screen.tracer(0)

ship = turtle.Turtle(); ship.shape("triangle"); ship.color("cyan"); ship.penup()
ship_speed = 6

asteroids = []
frames = 0; alive = True; start = time.time()

keys = {}
def press(k): keys[k]=True
def release(k): keys[k]=False
for k in ["Up","Down","Left","Right"]:
    keys[k]=False
    screen.onkeypress(lambda kk=k: press(kk), k)
    screen.onkeyrelease(lambda kk=k: release(kk), k)
screen.listen()

def spawn_asteroid():
    a = turtle.Turtle(); a.shape("circle"); a.color("gray"); a.penup()
    a.goto(310, random.randint(-180, 180)); a.dx = -random.randint(3,6)
    asteroids.append(a)

while alive:
    if keys.get("Up", False): ship.sety(ship.ycor()+ship_speed)
    if keys.get("Down", False): ship.sety(ship.ycor()-ship_speed)
    if keys.get("Left", False): ship.setx(ship.xcor()-ship_speed)
    if keys.get("Right", False): ship.setx(ship.xcor()+ship_speed)

    ship.setx(max(-280, min(280, ship.xcor())))
    ship.sety(max(-180, min(180, ship.ycor())))

    if frames % 20 == 0: spawn_asteroid()

    for a in list(asteroids):
        a.setx(a.xcor() + a.dx)
        if a.xcor() < -320:
            a.hideturtle(); asteroids.remove(a)
        elif ship.distance(a) < 20:
            alive = False; break

    screen.update(); time.sleep(0.03); frames += 1

survival = time.time() - start
print(f"You survived {survival:.1f} seconds!")
screen.exitonclick()
