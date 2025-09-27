import turtle
t = turtle.Turtle()

# small square (50)
t.forward(50); t.right(90)
t.forward(50); t.right(90)
t.forward(50); t.right(90)
t.forward(50); t.right(90)

# move aside, no drawing
t.penup(); t.goto(120, 0); t.pendown()

# medium square (100)
t.forward(100); t.right(90)
t.forward(100); t.right(90)
t.forward(100); t.right(90)
t.forward(100); t.right(90)

# move aside again
t.penup(); t.goto(260, 0); t.pendown()

# large square (150)
t.forward(150); t.right(90)
t.forward(150); t.right(90)
t.forward(150); t.right(90)
t.forward(150); t.right(90)

turtle.done()
