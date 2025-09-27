# Tiny Turtle demo: two groups of dots; click to add a test point and color it by nearest neighbor.
import turtle, math

screen = turtle.Screen(); screen.setup(800,600); screen.title('KNN Intro (Turtle)')
groups = {'red': [(-200,-50), (-180,20), (-150,-10), (-120,40)],
          'blue':[(160,70), (180,10), (200,50), (140,0)]}

pen = turtle.Turtle(); pen.hideturtle(); pen.speed(0)
dot = turtle.Turtle(); dot.hideturtle(); dot.speed(0)

def draw_groups():
    pen.clear()
    for color, pts in groups.items():
        for x,y in pts:
            dot.penup(); dot.goto(x,y); dot.dot(16, color)
    pen.penup(); pen.goto(-380, -260)
    pen.write("Click to add a test point", font=('Arial', 12, 'normal'))

def nearest_label(x,y):
    best = None
    for color, pts in groups.items():
        for px,py in pts:
            d = math.hypot(px-x, py-y)
            if best is None or d < best[0]:
                best = (d, color)
    return best[1]

def add_point(x,y):
    label = nearest_label(x,y)
    dot.penup(); dot.goto(x,y); dot.dot(18, label)

screen.onclick(add_point)
draw_groups()
turtle.done()
