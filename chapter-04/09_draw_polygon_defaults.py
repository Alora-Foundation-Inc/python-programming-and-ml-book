import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(6)

def draw_polygon(sides, size=50, color="black"):
    my_turtle.color(color)
    angle = 360 / sides
    for _ in range(sides):
        my_turtle.forward(size)
        my_turtle.right(angle)

draw_polygon(6)                  # hexagon with defaults
draw_polygon(8, 70)              # octagon, custom size
draw_polygon(5, 40, "purple")    # pentagon, custom all
draw_polygon(4, color="orange") # square, custom color only

turtle.done()
