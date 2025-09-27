import turtle
my_turtle = turtle.Turtle(); my_turtle.speed(7)

flowers = [
    {"x": 50, "y": 100, "color": "red", "petals": 6, "size": 25},
    {"x":150, "y":  50, "color": "blue","petals": 8, "size": 30},
    {"x":-100,"y":  75, "color": "yellow","petals": 5, "size": 20},
    {"x":  0, "y": -50, "color": "purple","petals": 7, "size": 35}
]

def move_to(x, y):
    my_turtle.penup(); my_turtle.goto(x, y); my_turtle.pendown()

def draw_flower(petals, size):
    for _ in range(petals):
        my_turtle.circle(size, 60); my_turtle.left(120)
        my_turtle.circle(size, 60); my_turtle.left(120)
        my_turtle.right(360 / petals)

for f in flowers:
    move_to(f["x"], f["y"]); my_turtle.color(f["color"]); draw_flower(f["petals"], f["size"])

turtle.done()
