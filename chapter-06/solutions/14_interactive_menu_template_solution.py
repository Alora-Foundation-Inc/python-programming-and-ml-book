import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

while True:
    cmd = screen.textinput("Menu", "square/circle/triangle/clear/quit")
    if cmd is None:
        continue
    if cmd == "square":
        for _ in range(4): artist.forward(50); artist.right(90)
    elif cmd == "circle":
        artist.circle(25)
    elif cmd == "triangle":
        for _ in range(3): artist.forward(50); artist.right(120)
    elif cmd == "clear":
        artist.clear()
    elif cmd == "quit":
        break
    else:
        print("Unknown command")

screen.mainloop()
