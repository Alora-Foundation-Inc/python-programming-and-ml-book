import turtle
t = turtle.Turtle()
t.speed(7)

sizes = [50, 75, 100, 125, 100, 75, 50]
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

for i in range(len(sizes)):
    t.color(colors[i])
    t.circle(sizes[i])
    t.right(51)

turtle.done()
