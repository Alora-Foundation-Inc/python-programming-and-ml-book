import turtle

t = turtle.Turtle()

side_length = 100
turn_angle = 90

# Repeat the two instructions 4 times
for i in range(4):
    t.forward(side_length)
    t.right(turn_angle)

turtle.done()
