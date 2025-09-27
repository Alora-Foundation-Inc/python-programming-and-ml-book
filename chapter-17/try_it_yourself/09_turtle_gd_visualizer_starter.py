# Turtle interactive: click to add points; press 'g' to run a few GD steps to fit y = m x + b.
# Keep it minimal and kid-friendly.
import turtle

points = []
m, b = 0.0, 0.0
lr = 0.0005

screen = turtle.Screen(); screen.setup(800,600); screen.title("Gradient Descent Visualizer (Turtle)")
pen = turtle.Turtle(); pen.hideturtle(); pen.speed(0)
dot = turtle.Turtle(); dot.hideturtle(); dot.speed(0)

def draw_axes():
    pen.clear()
    pen.penup(); pen.goto(-380,0); pen.pendown(); pen.forward(760)   # x-axis
    pen.penup(); pen.goto(0,-280); pen.setheading(90); pen.pendown(); pen.forward(560)  # y-axis
    pen.penup()
    # draw points
    for x,y in points:
        dot.penup(); dot.goto(x,y); dot.dot(6)

def add_point(x, y):
    points.append((x,y))
    draw_axes()

def gd_step():
    global m,b
    if not points: return
    # map turtle coords directly as x,y
    n = len(points)
    dm = sum(((m*x + b) - y)*x for x,y in points) * (2/n)
    db = sum(((m*x + b) - y)   for x,y in points) * (2/n)
    m -= lr*dm
    b -= lr*db
    # draw line
    draw_axes()
    line = turtle.Turtle(); line.hideturtle(); line.speed(0)
    xs = [-380, 380]
    for i,xp in enumerate(xs):
        yp = m*xp + b
        if i==0:
            line.penup(); line.goto(xp, yp); line.pendown()
        else:
            line.goto(xp, yp)

def run_gd_steps():
    for _ in range(30):
        gd_step()

screen.onclick(add_point)
screen.onkey(run_gd_steps, "g")
screen.listen()
draw_axes()
turtle.done()
