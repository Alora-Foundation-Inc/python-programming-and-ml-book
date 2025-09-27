import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

try:
    size = int(input("Enter a number for square size: "))
    if size > 0:
        for _ in range(4):
            artist.forward(size)
            artist.right(90)
        print("Square drawn!")
    else:
        print("Size must be positive!")
except ValueError:
    print("That's not a valid number! Please enter a whole number.")

screen.exitonclick()
