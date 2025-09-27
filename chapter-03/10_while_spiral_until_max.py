import turtle
t = turtle.Turtle()
t.speed(6)

distance = 10
max_distance = 100

while distance < max_distance:
    t.forward(distance)
    t.right(90)
    distance = distance + 5

turtle.done()
