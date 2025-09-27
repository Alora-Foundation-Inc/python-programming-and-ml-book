import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(9)

def draw_flower(petals, size, color):
    my_turtle.color(color)
    angle = 360 / petals
    for _ in range(petals):
        my_turtle.circle(size, 60)  # half-petal arc
        my_turtle.left(120)
        my_turtle.circle(size, 60)  # second half
        my_turtle.left(180 - 120)   # re-align
        my_turtle.right(angle)      # rotate to next petal

# Examples
draw_flower(6, 30, "magenta")
my_turtle.penup(); my_turtle.goto(140, 0); my_turtle.pendown()
draw_flower(8, 20, "orange")

turtle.done()
