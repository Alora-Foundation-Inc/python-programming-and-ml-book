# Choose pattern: spiral, flower, or star; choose color; repeat until 'quit'
import turtle

screen = turtle.Screen()
artist = turtle.Turtle()
artist.speed(0)

def pattern_spiral(color):
    artist.color(color)
    d = 2
    for _ in range(120):
        artist.forward(d); artist.right(91); d += 1

def pattern_flower(color):
    artist.color(color)
    for _ in range(12):
        artist.circle(40); artist.right(30)

def pattern_starburst(color):
    artist.color(color)
    for _ in range(36):
        artist.forward(120); artist.backward(120); artist.right(10)

while True:
    kind = input("Pattern (spiral/flower/star or 'quit')? ")
    if kind == "quit":
        break
    color = input("Color? ")
    if kind == "spiral":
        pattern_spiral(color)
    elif kind == "flower":
        pattern_flower(color)
    elif kind == "star":
        pattern_starburst(color)
    else:
        print("Try: spiral, flower, or star.")

screen.exitonclick()
