import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

print("Interactive Drawing Program!")
print("Commands: square, circle, triangle, clear, quit")

while True:
    command = screen.textinput("Draw", "What would you like to draw? (square/circle/triangle/clear/quit)")
    if command is None:
        continue

    if command == "square":
        for _ in range(4):
            artist.forward(50)
            artist.right(90)
        print("Square drawn!")

    elif command == "circle":
        artist.circle(25)
        print("Circle drawn!")

    elif command == "triangle":
        for _ in range(3):
            artist.forward(50)
            artist.right(120)
        print("Triangle drawn!")

    elif command == "clear":
        artist.clear()
        print("Screen cleared!")

    elif command == "quit":
        print("Goodbye!")
        break

    else:
        print("Unknown command. Try: square, circle, triangle, clear, quit")

screen.mainloop()
