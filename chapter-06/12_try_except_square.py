import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

try:
    size_text = input("Enter a number for square size: ")
    size = int(size_text)

    if size > 0:
        for _ in range(4):
            artist.forward(size)
            artist.right(90)
        print("Square drawn!")
    else:
        print("Size must be positive!")

except:
    print("That's not a valid number! Please enter a whole number.")

screen.exitonclick()
