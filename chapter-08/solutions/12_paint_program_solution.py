import turtle

screen = turtle.Screen(); screen.setup(800, 600); screen.bgcolor("white")
artist = turtle.Turtle(); artist.shape("circle"); artist.color("black"); artist.speed(0); artist.penup()

brush = {"down": False, "size": 3}

def start(x,y):
    brush["down"] = True
    artist.goto(x,y); artist.pendown()

def drag(x,y):
    if brush["down"]:
        artist.ondrag(None)
        artist.goto(x,y)
        artist.ondrag(drag)

def stop(x,y):
    brush["down"]=False; artist.penup()

def set_color(c): artist.color(c)
def set_size(sz): artist.pensize(sz); brush["size"]=sz
def clear(): artist.clear()

# Colors
screen.onkeypress(lambda: set_color("red"), "r")
screen.onkeypress(lambda: set_color("green"), "g")
screen.onkeypress(lambda: set_color("blue"), "b")
screen.onkeypress(lambda: set_color("purple"), "p")
screen.onkeypress(lambda: set_color("black"), "k")

# Sizes (1..9)
for n in "123456789":
    screen.onkeypress(lambda nn=n: set_size(int(nn)), n)

screen.onkeypress(clear, "space")
screen.listen()

screen.onscreenclick(start, 1)
artist.ondrag(drag)
screen.onscreenclick(stop, 3)

screen.mainloop()
