import turtle, random

screen = turtle.Screen()
artist = turtle.Turtle()

def flower():
    for _ in range(6): artist.circle(20); artist.right(60)

def star():
    for _ in range(5): artist.forward(50); artist.right(144)

while True:
    choice = screen.textinput("Studio", "flower/star/circle/random/clear/quit")
    if choice is None: continue
    if choice == "flower": flower()
    elif choice == "star": star()
    elif choice == "circle": artist.circle(30)
    elif choice == "random": artist.color(random.choice(["red","blue","green","purple"]))
    elif choice == "clear": artist.clear()
    elif choice == "quit": break

screen.mainloop()
