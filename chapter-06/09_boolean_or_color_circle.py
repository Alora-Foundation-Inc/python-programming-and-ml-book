import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

color = input("Enter red or blue: ")

if color == "red" or color == "blue":
    artist.color(color)
    artist.circle(30)
    print("Nice color choice!")
else:
    print("Please choose red or blue.")

screen.exitonclick()
