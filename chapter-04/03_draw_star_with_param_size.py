import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(6)

def draw_star(size):
    """Draw a 5-pointed star with the given size."""
    for _ in range(5):
        my_turtle.forward(size)
        my_turtle.right(144)

# Different sizes
my_turtle.color("red");   draw_star(30)
my_turtle.penup(); my_turtle.goto(100, 100); my_turtle.pendown()
my_turtle.color("blue");  draw_star(80)
my_turtle.penup(); my_turtle.goto(-100, 50); my_turtle.pendown()
my_turtle.color("green"); draw_star(50)

turtle.done()
