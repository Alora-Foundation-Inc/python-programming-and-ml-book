import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(6)

def draw_star():
    """Draw a 5-pointed star (fixed size)."""
    for _ in range(5):
        my_turtle.forward(50)
        my_turtle.right(144)

# Use our function multiple times
my_turtle.color("red");   draw_star()
my_turtle.penup(); my_turtle.goto(100, 100); my_turtle.pendown()
my_turtle.color("blue");  draw_star()
my_turtle.penup(); my_turtle.goto(-100, 50); my_turtle.pendown()
my_turtle.color("green"); draw_star()

turtle.done()
