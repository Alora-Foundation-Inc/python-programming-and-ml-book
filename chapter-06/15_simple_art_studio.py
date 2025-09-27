import turtle
import random

screen = turtle.Screen()
artist = turtle.Turtle()

def draw_flower():
    for _ in range(6):
        artist.circle(20)
        artist.right(60)

def draw_star():
    for _ in range(5):
        artist.forward(50)
        artist.right(144)

print("Welcome to Your Art Studio!")
print("Options: flower, star, circle, random, clear, quit")

while True:
    choice = screen.textinput("Studio", "What would you like to create? (flower/star/circle/random/clear/quit)")
    if choice is None:
        continue

    if choice == "flower":
        draw_flower()
        print("Flower created!")
    elif choice == "star":
        draw_star()
        print("Star created!")
    elif choice == "circle":
        artist.circle(30)
        print("Circle created!")
    elif choice == "random":
        artist.color(random.choice(["red", "blue", "green", "purple"]))
        print("Random color set!")
    elif choice == "clear":
        artist.clear()
        print("Canvas cleared!")
    elif choice == "quit":
        print("Thanks for creating art!")
        break
    else:
        print("Try: flower, star, circle, random, clear, quit")

screen.mainloop()
