import turtle
screen = turtle.Screen(); screen.setup(600,600); screen.title("Coordinate Plane — Turtle")
pen = turtle.Turtle(); pen.speed(0)

# axes
pen.pensize(2); pen.color("black")
pen.penup(); pen.goto(-280, 0); pen.pendown(); pen.forward(560)
pen.penup(); pen.goto(0, -280); pen.setheading(90); pen.pendown(); pen.forward(560)

# points
points = {"A":(0,0), "B":(60, 40), "C":(-80, 20), "D":(40,-60)}
dot = turtle.Turtle(); dot.shape("circle"); dot.color("blue"); dot.penup()

for name,(x,y) in points.items():
    dot.goto(x,y); dot.stamp()
    pen.penup(); pen.goto(x+6, y+6); pen.write(name, font=("Arial", 10, "normal"))

print("Close the window to finish.")
screen.exitonclick()
