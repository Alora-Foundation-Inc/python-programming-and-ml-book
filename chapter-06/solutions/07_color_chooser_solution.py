import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

color_choice = input("Pick a color (red/blue/green/purple): ")
colors = ["red","blue","green","purple"]

if color_choice in colors:
    artist.color(color_choice)
else:
    print("Using default black color.")
    artist.color("black")

for _ in range(4):
    artist.forward(80)
    artist.right(90)

screen.exitonclick()
