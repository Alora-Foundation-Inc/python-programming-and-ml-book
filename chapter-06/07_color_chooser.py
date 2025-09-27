import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

color_choice = input("Pick a color (red/blue/green/purple): ")

if color_choice == "red":
    artist.color("red")
elif color_choice == "blue":
    artist.color("blue")
elif color_choice == "green":
    artist.color("green")
elif color_choice == "purple":
    artist.color("purple")
else:
    print("Using default black color.")
    artist.color("black")

for _ in range(4):
    artist.forward(80)
    artist.right(90)

screen.exitonclick()
