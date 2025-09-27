import turtle

screen = turtle.Screen(); screen.setup(600, 400); screen.bgcolor("black")
artist = turtle.Turtle(); artist.shape("circle"); artist.color("white"); artist.speed(0); artist.penup()

drawing = False

def start_draw(x, y):
    global drawing
    drawing = True
    artist.goto(x, y); artist.pendown()

def keep_drawing(x, y):
    if drawing:
        artist.ondrag(None)      # prevent event overlap
        artist.goto(x, y)
        artist.ondrag(keep_drawing)

def stop_draw(x, y):
    global drawing
    drawing = False
    artist.penup()

screen.onscreenclick(start_draw, 1)   # left click
artist.ondrag(keep_drawing)
screen.onscreenclick(stop_draw, 3)    # right click
print("Left-drag to draw; right-click to stop.")
screen.mainloop()
