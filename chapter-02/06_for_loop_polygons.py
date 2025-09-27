import turtle

t = turtle.Turtle()
t.speed(6)

# Triangle (3 sides): angle = 360 / 3 = 120
for i in range(3):
    t.forward(100)
    t.right(120)

# Move to a new position
t.penup(); t.goto(150, 0); t.pendown()

# Hexagon (6 sides): angle = 360 / 6 = 60
for i in range(6):
    t.forward(80)
    t.right(60)

turtle.done()
