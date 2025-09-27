import turtle
t = turtle.Turtle()

# square at (0,0)
t.goto(0, 0)
t.forward(80); t.right(90)
t.forward(80); t.right(90)
t.forward(80); t.right(90)
t.forward(80); t.right(90)

# square at (140, 0)
t.penup(); t.goto(140, 0); t.pendown()
t.color("green")
t.forward(80); t.right(90)
t.forward(80); t.right(90)
t.forward(80); t.right(90)
t.forward(80); t.right(90)

# square at (70, 120)
t.penup(); t.goto(70, 120); t.pendown()
t.color("purple"); t.pensize(4)
t.forward(80); t.right(90)
t.forward(80); t.right(90)
t.forward(80); t.right(90)
t.forward(80); t.right(90)

turtle.done()
