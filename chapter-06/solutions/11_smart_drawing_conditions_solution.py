import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

size = int(input("Enter size (10-100): "))
color = input("Enter color (red/blue/green): ")

valid_color = color in ["red","blue","green"]
valid_size = 10 <= size <= 100

if valid_size and valid_color:
    artist.color(color)
    for _ in range(4):
        artist.forward(size)
        artist.right(90)
    print("Perfect! Square drawn!")
else:
    print("Either size or color is invalid.")

screen.exitonclick()
