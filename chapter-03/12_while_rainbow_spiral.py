import turtle
t = turtle.Turtle()
t.speed(9)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
color_index = 0
side_length = 5

while side_length < 150:
    t.color(colors[color_index % len(colors)])
    t.forward(side_length)
    t.right(91)
    side_length = side_length + 2
    color_index = color_index + 1

turtle.done()
