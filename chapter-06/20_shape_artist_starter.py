# Ask the user for shape, size, and color. Draw until 'quit'.
# Shapes: square, triangle, pentagon.
import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

print("Type 'quit' any time to stop.")

while True:
    shape = input("Shape (square/triangle/pentagon or 'quit')? ")
    if shape == "quit":
        break
    size = int(input("Size? "))
    color = input("Color? ")
    artist.color(color)

    if shape == "square":
        for _ in range(4): artist.forward(size); artist.right(90)
    elif shape == "triangle":
        for _ in range(3): artist.forward(size); artist.right(120)
    elif shape == "pentagon":
        for _ in range(5): artist.forward(size); artist.right(72)
    else:
        print("Unknown shape.")

screen.exitonclick()
