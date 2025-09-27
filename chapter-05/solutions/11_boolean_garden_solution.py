import turtle
my_turtle = turtle.Turtle(); my_turtle.speed(8)

items = [
    {"type": "flower", "x": -120, "y": 80, "water_needed": True, "sun_needed": True},
    {"type": "mushroom", "x": -20, "y": 30, "water_needed": True, "sun_needed": False},
    {"type": "cactus", "x": 100, "y": -40, "water_needed": False, "sun_needed": True},
    {"type": "fern", "x": 0, "y": 0, "water_needed": True, "sun_needed": False},
]

has_rain = True
has_sun = True

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

for it in items:
    move_to(it["x"], it["y"])
    if it["water_needed"] and it["sun_needed"]:
        healthy = has_rain and has_sun
    elif it["water_needed"] or it["sun_needed"]:
        healthy = has_rain or has_sun
    else:
        healthy = True
    draw_item(it["type"], healthy)

turtle.done()
