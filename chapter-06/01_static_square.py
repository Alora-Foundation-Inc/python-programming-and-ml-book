import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

for _ in range(4):
    artist.forward(100)
    artist.right(90)

screen.exitonclick()
