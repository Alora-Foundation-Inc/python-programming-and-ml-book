import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(6)

def calculate_star_angle():
    return 144

def calculate_spiral_distance(step):
    return step * 3 + 10

def draw_star(size):
    angle = calculate_star_angle()
    for _ in range(5):
        my_turtle.forward(size)
        my_turtle.right(angle)

def draw_spiral(steps):
    for step in range(steps):
        dist = calculate_spiral_distance(step)
        my_turtle.forward(dist)
        my_turtle.right(90)

draw_star(60)
my_turtle.penup(); my_turtle.goto(120, 120); my_turtle.pendown()
draw_spiral(20)

turtle.done()
