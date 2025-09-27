import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

sides = int(input("How many sides (3–20)? "))

if 3 <= sides <= 20:
    angle = 360 / sides
    for _ in range(sides):
        artist.forward(50)
        artist.right(angle)
    print("Polygon drawn!")
else:
    print("Please choose between 3 and 20 sides.")

screen.exitonclick()
