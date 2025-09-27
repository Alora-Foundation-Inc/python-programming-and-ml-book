import turtle
my_turtle = turtle.Turtle(); my_turtle.speed(7)

flowers = [
    [50, 100, "red", 6],
    [150,  50, "blue", 8],
    [-100, 75, "yellow", 5],
    [0,   -50, "purple", 7],
    [-150,100, "pink", 6]
]

def move_to(x, y):
    my_turtle.penup(); my_turtle.goto(x, y); my_turtle.pendown()

def draw_flower(petals, size=25):
    for _ in range(petals):
        my_turtle.circle(size, 60); my_turtle.left(120)
        my_turtle.circle(size, 60); my_turtle.left(120)
        my_turtle.right(360 / petals)

for x, y, color, petals in flowers:
    move_to(x, y); my_turtle.color(color); draw_flower(petals)

turtle.done()
