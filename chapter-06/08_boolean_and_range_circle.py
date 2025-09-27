import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

size = int(input("Enter a size between 10 and 50: "))

if size >= 10 and size <= 50:
    artist.circle(size)
    print("Perfect size!")
else:
    print("Size must be between 10 and 50.")

screen.exitonclick()
