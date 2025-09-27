import turtle

t = turtle.Turtle()
t.speed(8)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
radius = 60

# Draw 6 overlapping circles, turning 60° each time
for i in range(6):
    t.color(colors[i % len(colors)])
    t.circle(radius)
    t.right(60)  # 360 / 6

turtle.done()
