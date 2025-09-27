import turtle

t = turtle.Turtle()
t.speed(8)
t.color("purple")

distance = 5
angle = 91  # slightly more than 90 creates a spiral

for i in range(100):
    t.forward(distance)
    t.right(angle)
    distance = distance + 1  # make each step a bit longer

turtle.done()
