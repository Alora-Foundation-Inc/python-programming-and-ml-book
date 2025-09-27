import turtle
t = turtle.Turtle()
t.speed(9)

def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.right(144)

def draw_flower(petals, size):
    angle = 360 / petals
    for _ in range(petals):
        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.left(180 - 120)
        t.right(angle)

def draw_pattern(kind, repeats=10, size=50, color_list=None):
    if color_list is None:
        color_list = ["red","orange","yellow","green","blue","purple"]
    if kind == "star":
        for i in range(repeats):
            t.color(color_list[i % len(color_list)])
            t.penup(); t.goto(0,0); t.pendown()
            t.setheading(i * (360/repeats))
            t.forward(size*2)
            draw_star(size)
    elif kind == "spiral":
        angle = 91
        dist = 1
        for i in range(repeats*10):
            t.color(color_list[i % len(color_list)])
            t.forward(dist); t.right(angle); dist += 1
    elif kind == "flowers":
        for i in range(repeats):
            t.color(color_list[i % len(color_list)])
            t.penup(); t.goto(0,0); t.pendown()
            t.setheading(i * (360/repeats))
            t.forward(size*2)
            draw_flower(6, size//3)

# Examples
draw_pattern("star", repeats=12, size=30)

turtle.done()
