# Demonstrates why separate variables become messy fast.
import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(7)

# messy variables
flower1_x, flower1_y, flower1_color, flower1_petals = 50, 100, "red", 6
flower2_x, flower2_y, flower2_color, flower2_petals = 150, 50, "blue", 8
flower3_x, flower3_y, flower3_color, flower3_petals = -100, 75, "yellow", 5

def move_to(x, y):
    my_turtle.penup(); my_turtle.goto(x, y); my_turtle.pendown()

def draw_flower(petals, size=25):
    for _ in range(petals):
        my_turtle.circle(size, 60); my_turtle.left(120)
        my_turtle.circle(size, 60); my_turtle.left(120)
        my_turtle.right(360 / petals)

# draw 3 flowers (repetitive!)
move_to(flower1_x, flower1_y); my_turtle.color(flower1_color); draw_flower(flower1_petals)
move_to(flower2_x, flower2_y); my_turtle.color(flower2_color); draw_flower(flower2_petals)
move_to(flower3_x, flower3_y); my_turtle.color(flower3_color); draw_flower(flower3_petals)

turtle.done()
