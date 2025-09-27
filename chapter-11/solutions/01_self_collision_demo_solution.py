import turtle

screen = turtle.Screen(); screen.setup(600,600); screen.bgcolor("black"); screen.tracer(0)
head = turtle.Turtle(); head.shape("square"); head.color("lime"); head.penup(); head.goto(0,0)

segments = []
for i in range(1,5):
    s = turtle.Turtle(); s.shape("square"); s.color("lightgreen"); s.penup(); s.goto(i*20,0)
    segments.append(s)

def check_self_collision(distance_limit=20):
    for seg in segments:
        if head.distance(seg) < distance_limit:
            print("COLLISION!"); seg.color("yellow"); return True
    return False

# Test three positions
for x in [0, 20, 40]:
    head.goto(x,0); screen.update()
    print(f"Head at {x}, collide? ->", check_self_collision())

screen.exitonclick()
