import turtle

t = turtle.Turtle()
t.speed(6)

sizes = [50, 75, 100, 125, 150]

for size in sizes:
    # draw one square
    for side in range(4):
        t.forward(size)
        t.right(90)

    # move forward for spacing
    t.penup()
    t.forward(size + 20)
    t.pendown()

turtle.done()
