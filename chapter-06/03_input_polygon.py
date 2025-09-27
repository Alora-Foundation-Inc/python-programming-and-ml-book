import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

sides = int(input("How many sides for your polygon? "))
angle = 360 / sides

for _ in range(sides):
    artist.forward(50)
    artist.right(angle)

screen.exitonclick()
