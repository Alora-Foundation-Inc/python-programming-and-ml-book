import turtle

t = turtle.Turtle()

# Move without drawing to (50, 50), then draw
t.penup()
t.goto(50, 50)
t.pendown()
t.forward(80)

# Jump to a new spot and draw again
t.penup()
t.goto(-100, -50)
t.pendown()
t.right(90)
t.forward(120)

turtle.done()
