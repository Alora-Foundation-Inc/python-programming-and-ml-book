import turtle
my_turtle = turtle.Turtle(); my_turtle.speed(9)

def move_to(x, y): my_turtle.penup(); my_turtle.goto(x, y); my_turtle.pendown()

def draw_spiral(steps=80, start=2, angle=91, color="purple"):
    my_turtle.color(color)
    d = start
    for _ in range(steps):
        my_turtle.forward(d); my_turtle.right(angle); d += 1

def draw_mandala(spokes=12, radius=80, color_list=None):
    if color_list is None: color_list=["red","orange","yellow","green","blue","purple"]
    ang = 360/spokes
    for i in range(spokes):
        my_turtle.color(color_list[i % len(color_list)])
        my_turtle.penup(); my_turtle.goto(0,0); my_turtle.pendown()
        my_turtle.setheading(i*ang); my_turtle.forward(radius)
        my_turtle.right(30); my_turtle.forward(20); my_turtle.backward(20)
        my_turtle.left(60);  my_turtle.forward(20); my_turtle.backward(20)

def draw_polygon(sides=6, size=60, color="teal"):
    my_turtle.color(color)
    ang = 360/sides
    for _ in range(sides):
        my_turtle.forward(size); my_turtle.right(ang)

library = {
    "spiral":  {"fn":"spiral",  "params":{"steps":90,"start":2,"angle":91,"color":"purple"}},
    "mandala": {"fn":"mandala", "params":{"spokes":16,"radius":90,"color_list":["red","gold","cyan","magenta"]}},
    "polygon": {"fn":"polygon", "params":{"sides":7,"size":70,"color":"teal"}}
}

# Draw all patterns in a row
x = -200
for name, spec in library.items():
    move_to(x, 0)
    if spec["fn"] == "spiral":
        draw_spiral(**spec["params"])
    elif spec["fn"] == "mandala":
        draw_mandala(**spec["params"])
    elif spec["fn"] == "polygon":
        draw_polygon(**spec["params"])
    x += 200

# Save a tiny "export" of pattern names and params
with open("pattern_library.txt","w",encoding="utf-8") as f:
    for name, spec in library.items():
        f.write(f"{name}:{spec['params']}\n")

print("Pattern library saved.")

turtle.done()
