import turtle

t = turtle.Turtle()

# Variables make code easy to change
side_length = 100
turn_angle = 90  # change to 60 for a hexagon

# Draw 4 sides using the variables (still without a loop, to compare)
t.forward(side_length); t.right(turn_angle)
t.forward(side_length); t.right(turn_angle)
t.forward(side_length); t.right(turn_angle)
t.forward(side_length); t.right(turn_angle)

turtle.done()
