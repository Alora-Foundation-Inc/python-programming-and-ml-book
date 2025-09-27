import turtle
t = turtle.Turtle()
t.speed(8)

rows = 4
columns = 5
square_size = 30
spacing = 10

# start at origin; we will go row by row downward
for row in range(rows):
    # draw one row
    for col in range(columns):
        # draw one square
        for _ in range(4):
            t.forward(square_size)
            t.right(90)
        # move to next column
        t.penup()
        t.forward(square_size + spacing)
        t.pendown()
    # move to next row start
    t.penup()
    t.goto(0, -(row + 1) * (square_size + spacing))
    t.pendown()

turtle.done()
