import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

size = int(input("Square size? "))

if size > 0:
    for _ in range(4):
        artist.forward(size)
        artist.right(90)
    print("Square drawn!")

screen.exitonclick()
