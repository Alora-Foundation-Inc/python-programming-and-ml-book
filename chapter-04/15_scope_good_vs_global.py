import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(7)

# Good: uses parameters (self-contained)
def draw_star(size, color):
    my_turtle.color(color)
    for _ in range(5):
        my_turtle.forward(size)
        my_turtle.right(144)

draw_star(50, "blue")
my_turtle.penup(); my_turtle.goto(120, 0); my_turtle.pendown()
draw_star(100, "gold")

turtle.done()
