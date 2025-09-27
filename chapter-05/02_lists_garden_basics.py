# Use parallel lists to organize related info.
import turtle
my_turtle = turtle.Turtle(); my_turtle.speed(7)

flower_x = [50, 150, -100, 0, -150]
flower_y = [100, 50, 75, -50, 100]
flower_colors = ["red", "blue", "yellow", "purple", "pink"]
flower_petals = [6, 8, 5, 7, 6]

def move_to(x, y):
    my_turtle.penup(); my_turtle.goto(x, y); my_turtle.pendown()

def draw_flower(petals, size=25):
    for _ in range(petals):
        my_turtle.circle(size, 60); my_turtle.left(120)
        my_turtle.circle(size, 60); my_turtle.left(120)
        my_turtle.right(360 / petals)

for i in range(len(flower_x)):
    move_to(flower_x[i], flower_y[i])
    my_turtle.color(flower_colors[i])
    draw_flower(flower_petals[i])

turtle.done()
