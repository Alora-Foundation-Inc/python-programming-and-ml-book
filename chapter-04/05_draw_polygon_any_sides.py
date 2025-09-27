import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(6)

def draw_polygon(sides, size, color):
    """Draw a regular polygon with given sides, size, and color."""
    my_turtle.color(color)
    angle = 360 / sides
    for _ in range(sides):
        my_turtle.forward(size)
        my_turtle.right(angle)

draw_polygon(3, 80, "red")     # triangle
my_turtle.penup(); my_turtle.goto(150, 0); my_turtle.pendown()
draw_polygon(6, 60, "blue")    # hexagon
my_turtle.penup(); my_turtle.goto(-150, 0); my_turtle.pendown()
draw_polygon(8, 50, "green")   # octagon

turtle.done()
