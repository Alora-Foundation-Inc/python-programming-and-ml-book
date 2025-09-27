import turtle
my_turtle = turtle.Turtle(); my_turtle.speed(8)

garden_items = [
    {"type": "flower",  "x": 50,  "y": 100, "water_needed": True,  "sun_needed": True},
    {"type": "mushroom","x":-50,  "y": 50,  "water_needed": True,  "sun_needed": False},
    {"type": "cactus",  "x": 100, "y":-50,  "water_needed": False, "sun_needed": True},
    {"type": "fern",    "x":-100, "y": 0,   "water_needed": True,  "sun_needed": False},
]

has_rain = True
has_sun  = False

def move_to(x, y):
    my_turtle.penup(); my_turtle.goto(x, y); my_turtle.pendown()

def draw_item(kind, healthy):
    if kind == "flower":
        my_turtle.color("red" if healthy else "brown")
        for _ in range(6):
            my_turtle.circle(15, 60); my_turtle.left(120)
            my_turtle.circle(15, 60); my_turtle.left(120)
            my_turtle.right(60)
    elif kind == "mushroom":
        my_turtle.color("red" if healthy else "gray"); my_turtle.circle(20)
    elif kind == "cactus":
        my_turtle.color("green" if healthy else "yellow")
        my_turtle.left(90); my_turtle.forward(40); my_turtle.backward(40); my_turtle.right(90)
    elif kind == "fern":
        my_turtle.color("green" if healthy else "brown")
        for _ in range(4):
            my_turtle.forward(30); my_turtle.backward(30); my_turtle.right(90)

for item in garden_items:
    move_to(item["x"], item["y"])
    if item["water_needed"] and item["sun_needed"]:
        healthy = has_rain and has_sun
    elif item["water_needed"] or item["sun_needed"]:
        healthy = has_rain or has_sun
    else:
        healthy = True
    draw_item(item["type"], healthy)

turtle.done()
