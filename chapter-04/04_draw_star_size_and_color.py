import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(6)

def draw_star(size, color):
    """Draw a 5-pointed star with size and color."""
    my_turtle.color(color)
    for _ in range(5):
        my_turtle.forward(size)
        my_turtle.right(144)

draw_star(40, "red")
my_turtle.penup(); my_turtle.goto(100, 100); my_turtle.pendown()
draw_star(60, "blue")
my_turtle.penup(); my_turtle.goto(-100, 50); my_turtle.pendown()
draw_star(80, "green")

turtle.done()
