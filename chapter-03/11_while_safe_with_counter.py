import turtle
t = turtle.Turtle()
t.speed(8)

distance = 5
safety_counter = 0
max_iterations = 50

while distance < 200 and safety_counter < max_iterations:
    t.forward(distance)
    t.right(89)
    distance = distance + 2
    safety_counter = safety_counter + 1

turtle.done()
