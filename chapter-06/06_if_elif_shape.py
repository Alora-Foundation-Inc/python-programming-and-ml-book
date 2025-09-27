import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

shape = input("What shape? (square/triangle/circle): ")

if shape == "square":
    for _ in range(4):
        artist.forward(60)
        artist.right(90)
elif shape == "triangle":
    for _ in range(3):
        artist.forward(60)
        artist.right(120)
elif shape == "circle":
    artist.circle(30)
else:
    print("I don't know that shape.")

screen.exitonclick()
