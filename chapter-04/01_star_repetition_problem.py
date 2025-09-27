import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(6)

# Draw first star
my_turtle.color("red")
for i in range(5):
    my_turtle.forward(50)
    my_turtle.right(144)

# Move to new position
my_turtle.penup()
my_turtle.goto(100, 100)
my_turtle.pendown()

# Draw second star (same code again!)
my_turtle.color("blue")
for i in range(5):
    my_turtle.forward(50)
    my_turtle.right(144)

# Move to another position
my_turtle.penup()
my_turtle.goto(-100, 50)
my_turtle.pendown()

# Draw third star (same code yet again!)
my_turtle.color("green")
for i in range(5):
    my_turtle.forward(50)
    my_turtle.right(144)

turtle.done()
