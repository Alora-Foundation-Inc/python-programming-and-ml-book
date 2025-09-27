import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

valid_colors = ["red", "blue", "green", "yellow", "purple"]
while True:
    color = input(f"Choose a color {valid_colors}: ")
    if color in valid_colors:
        break
    print(f"Please choose from: {valid_colors}")

artist.color(color)
artist.circle(50)
print(f"Beautiful {color} circle!")

screen.exitonclick()
