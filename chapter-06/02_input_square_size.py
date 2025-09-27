import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

size_text = input("How big should the square be? ")
size = int(size_text)

for _ in range(4):
    artist.forward(size)
    artist.right(90)

screen.exitonclick()
