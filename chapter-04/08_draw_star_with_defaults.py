import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(6)

def draw_star(size=50, color="blue"):
    my_turtle.color(color)
    for _ in range(5):
        my_turtle.forward(size)
        my_turtle.right(144)

draw_star()            # uses defaults
draw_star(80)          # custom size, default color
draw_star(30, "red")  # custom both
draw_star(color="green")  # named argument

turtle.done()
