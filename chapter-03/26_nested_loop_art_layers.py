import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
palette = ["#ff6b6b","#ffd93d","#6bcB77","#4d96ff","#8352ff"]

layers = 4
shapes_per_layer = 12
sides = 6
radius = 60

for layer in range(layers):
    t.color(palette[layer % len(palette)])
    for k in range(shapes_per_layer):
        t.penup(); t.goto(0, 0); t.pendown()
        t.setheading(k * (360 / shapes_per_layer) + layer * 10)
        # draw a small hexagon motif
        for _ in range(sides):
            t.forward(radius + layer * 10)
            t.right(360 / sides)
    radius += 10

turtle.done()
