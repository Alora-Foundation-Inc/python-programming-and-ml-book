# A minimal working Turtle visualizer:
# Click to add points; press 'g' to run a few GD steps; 'c' to clear; '+'/'-' to tweak learning rate.
import turtle

points = []
m, b = 0.0, 0.0
lr = 0.0005

screen = turtle.Screen(); screen.setup(800,600); screen.title("GD Visualizer — Solution")
pen = turtle.Turtle(); pen.hideturtle(); pen.speed(0)
dot = turtle.Turtle(); dot.hideturtle(); dot.speed(0)

def draw():
    pen.clear()
    # axes
    pen.penup(); pen.goto(-380,0); pen.pendown(); pen.forward(760)
    pen.penup(); pen.goto(0,-280); pen.setheading(90); pen.pendown(); pen.forward(560)
    # points
    for x,y in points:
        dot.penup(); dot.goto(x,y); dot.dot(6)
    # line
    line = turtle.Turtle(); line.hideturtle(); line.speed(0)
    xs = [-380, 380]
    for i,xp in enumerate(xs):
        yp = m*xp + b
        if i==0:
            line.penup(); line.goto(xp, yp); line.pendown()
        else:
            line.goto(xp, yp)
    # HUD
    pen.penup(); pen.goto(-370, 260); pen.write(f"m={m:.4f}  b={b:.2f}  lr={lr:.5f}", font=("Arial", 12, "normal"))

def add_point(x, y):
    points.append((x,y))
    draw()

def gd_step():
    global m,b
    if not points: return
    n = len(points)
    dm = sum(((m*x + b) - y)*x for x,y in points) * (2/n)
    db = sum(((m*x + b) - y)   for x,y in points) * (2/n)
    m -= lr*dm
    b -= lr*db
    draw()

def run_steps():
    for _ in range(30):
        gd_step()

def clear_all():
    global points, m, b
    points = []; m = 0.0; b = 0.0
    draw()

def inc_lr():
    global lr; lr *= 1.2; draw()

def dec_lr():
    global lr; lr /= 1.2; draw()

screen.onclick(add_point)
screen.onkey(run_steps, "g")
screen.onkey(clear_all, "c")
screen.onkey(inc_lr, "+")
screen.onkey(dec_lr, "-")
screen.listen()
draw()
turtle.done()
