import turtle

t = turtle.Turtle()
t.speed(5); t.pensize(3)

side_length = 100
colors = ["red", "green", "blue"]  # 3 colors for 3 sides

for color in colors:
    t.color(color)
    t.forward(side_length)
    t.left(120)  # 360 / 3

turtle.done()
