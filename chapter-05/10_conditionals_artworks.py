import turtle
my_turtle = turtle.Turtle(); my_turtle.speed(7)

artworks = [
    {"type": "star",   "size": 50, "color": "gold",  "x": 0,   "y": 100},
    {"type": "circle", "size": 30, "color": "blue",  "x": 100, "y": 50},
    {"type": "star",   "size": 80, "color": "red",   "x":-100, "y": 0},
    {"type": "square", "size": 40, "color": "green", "x": 0,   "y":-50},
]

def move_to(x, y):
    my_turtle.penup(); my_turtle.goto(x, y); my_turtle.pendown()

def draw_star(size):
    for _ in range(5):
        my_turtle.forward(size)
        my_turtle.right(144)

def draw_circle(size):
    my_turtle.circle(size)

def draw_square(size):
    for _ in range(4):
        my_turtle.forward(size); my_turtle.right(90)

for art in artworks:
    move_to(art["x"], art["y"])
    my_turtle.color(art["color"])
    if art["type"] == "star":
        draw_star(art["size"])
    elif art["type"] == "circle":
        draw_circle(art["size"])
    elif art["type"] == "square":
        draw_square(art["size"])
    else:
        print("Unknown type:", art["type"])

turtle.done()
