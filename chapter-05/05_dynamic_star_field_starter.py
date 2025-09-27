# Create lists for star_x, star_y, star_sizes, star_colors and draw them.
import turtle
my_turtle = turtle.Turtle(); my_turtle.speed(9)

# TODO: make lists for positions, sizes, colors
star_x = []
star_y = []
star_sizes = []
star_colors = []

def move_to(x, y):
    my_turtle.penup(); my_turtle.goto(x, y); my_turtle.pendown()

def draw_star(size):
    for _ in range(5):
        my_turtle.forward(size)
        my_turtle.right(144)

# TODO: fill lists and loop to draw stars
# for i in range(len(star_x)):
#     move_to(star_x[i], star_y[i])
#     my_turtle.color(star_colors[i])
#     draw_star(star_sizes[i])

turtle.done()
