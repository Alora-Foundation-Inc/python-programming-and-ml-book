import turtle
t = turtle.Turtle()
t.speed(8)

for length in range(20, 121, 20):  # 20,40,60,80,100,120
    # draw one square of 'length'
    for _ in range(4):
        t.forward(length)
        t.right(90)
    # move aside for the next one
    t.penup()
    t.forward(length + 15)
    t.pendown()

turtle.done()
