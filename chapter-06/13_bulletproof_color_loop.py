import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

valid_colors = ["red", "blue", "green", "yellow", "purple"]
valid_input = False

while not valid_input:
    color = input(f"Choose a color {valid_colors}: ")
    if color in valid_colors:
        valid_input = True
    else:
        print(f"Please choose from: {valid_colors}")

artist.color(color)
artist.circle(50)
print(f"Beautiful {color} circle!")

screen.exitonclick()
