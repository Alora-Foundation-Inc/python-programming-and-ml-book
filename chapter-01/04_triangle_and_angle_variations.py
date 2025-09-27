import turtle
t = turtle.Turtle()

# Equilateral triangle
t.forward(120); t.right(120)
t.forward(120); t.right(120)
t.forward(120); t.right(120)

# Move to a new spot
t.penup(); t.goto(180, 0); t.pendown()

# “45-degree” turns — not a closed shape in 4 sides, but fun to see
t.forward(80); t.right(45)
t.forward(80); t.right(45)
t.forward(80); t.right(45)
t.forward(80); t.right(45)

turtle.done()
