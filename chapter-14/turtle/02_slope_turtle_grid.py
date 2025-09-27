import turtle
screen = turtle.Screen(); screen.setup(600,600); screen.title("Slope with Turtle")
pen = turtle.Turtle(); pen.speed(0)

# grid
pen.color("lightgray"); pen.pensize(1)
for x in range(-280, 300, 20):
    pen.penup(); pen.goto(x, -280); pen.pendown(); pen.goto(x, 280)
for y in range(-280, 300, 20):
    pen.penup(); pen.goto(-280, y); pen.pendown(); pen.goto(280, y)

# axes
pen.color("black"); pen.pensize(2)
pen.penup(); pen.goto(-280, 0); pen.pendown(); pen.goto(280,0)
pen.penup(); pen.goto(0, -280); pen.pendown(); pen.goto(0,280)

# example line y = (1/2)x + 20
line = turtle.Turtle(); line.color("red"); line.pensize(3); line.penup()
line.goto(-200, -100+20); line.pendown()
for x in range(-200, 220, 20):
    y = int(0.5*(x) + 20)  # (scaled)
    line.goto(x, y)

screen.exitonclick()
