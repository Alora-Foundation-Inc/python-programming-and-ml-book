import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(7)

def move_to(x, y):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()

def draw_circle(radius, color="black"):
    my_turtle.color(color)
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()

def draw_rectangle(width, height, color="black"):
    my_turtle.color(color)
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(width); my_turtle.right(90)
        my_turtle.forward(height); my_turtle.right(90)
    my_turtle.end_fill()

def draw_triangle(size, color="black"):
    my_turtle.color(color)
    my_turtle.begin_fill()
    for _ in range(3):
        my_turtle.forward(size); my_turtle.right(120)
    my_turtle.end_fill()

# Try it out
draw_circle(30, "red")
move_to(100, 0); draw_rectangle(50, 80, "blue")
move_to(-100, 0); draw_triangle(60, "green")

turtle.done()
