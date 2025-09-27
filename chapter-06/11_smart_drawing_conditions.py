import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

size = int(input("Enter size (10-100): "))
color = input("Enter color (red/blue/green): ")

if (10 <= size <= 100) and (color == "red" or color == "blue" or color == "green"):
    artist.color(color)
    for _ in range(4):
        artist.forward(size)
        artist.right(90)
    print("Perfect! Square drawn!")
else:
    print("Either size is wrong (10-100) or color is wrong (red/blue/green).")

screen.exitonclick()
