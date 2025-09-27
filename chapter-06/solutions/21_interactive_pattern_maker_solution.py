import turtle

screen = turtle.Screen()
artist = turtle.Turtle()
artist.speed(0)

def spiral(c):
    artist.color(c); d = 2
    for _ in range(120):
        artist.forward(d); artist.right(91); d += 1

def flower(c):
    artist.color(c)
    for _ in range(12):
        artist.circle(40); artist.right(30)

def starburst(c):
    artist.color(c)
    for _ in range(36):
        artist.forward(120); artist.backward(120); artist.right(10)

while True:
    kind = input("Pattern (spiral/flower/star or 'quit')? ")
    if kind == "quit": break
    color = input("Color? ")
    if kind == "spiral": spiral(color)
    elif kind == "flower": flower(color)
    elif kind == "star": starburst(color)
    else: print("Try: spiral, flower, or star.")

screen.exitonclick()
