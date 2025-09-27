import turtle
my_turtle = turtle.Turtle(); my_turtle.speed(9)

star_x = [0,  80, -120, 140, -60]
star_y = [0,  90,   60, -40, -80]
star_sizes = [30, 50, 40, 60, 35]
star_colors = ["gold","cyan","magenta","white","orange"]

def move_to(x, y):
    my_turtle.penup(); my_turtle.goto(x, y); my_turtle.pendown()

def draw_star(size):
    for _ in range(5):
        my_turtle.forward(size); my_turtle.right(144)

for i in range(len(star_x)):
    move_to(star_x[i], star_y[i])
    my_turtle.color(star_colors[i])
    draw_star(star_sizes[i])

turtle.done()
