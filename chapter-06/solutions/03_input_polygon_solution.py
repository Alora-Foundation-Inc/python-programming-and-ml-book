import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

sides = int(input("How many sides for your polygon? "))
if sides >= 3:
    angle = 360 / sides
    for _ in range(sides):
        artist.forward(50)
        artist.right(angle)
else:
    print("Polygons need at least 3 sides.")

screen.exitonclick()
