import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(7)

def draw_square(size, color):
    my_turtle.color(color)
    my_turtle.begin_fill()
    for _ in range(4):
        my_turtle.forward(size); my_turtle.right(90)
    my_turtle.end_fill()

def draw_triangle(size, color):
    my_turtle.color(color)
    my_turtle.begin_fill()
    for _ in range(3):
        my_turtle.forward(size); my_turtle.right(120)
    my_turtle.end_fill()

def draw_house(size=100, house_color="yellow", roof_color="red"):
    # base
    draw_square(size, house_color)
    # roof
    my_turtle.left(90); my_turtle.forward(size); my_turtle.right(90)  # move to top edge
    draw_triangle(size, roof_color)
    # reset to baseline
    my_turtle.right(90); my_turtle.forward(size); my_turtle.left(90)

# Examples
draw_house()
my_turtle.penup(); my_turtle.goto(140, 0); my_turtle.pendown()
draw_house(80, "lightblue", "purple")

turtle.done()
