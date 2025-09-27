import turtle

screen = turtle.Screen(); screen.setup(800, 600)
artist = turtle.Turtle(); artist.shape("circle"); artist.speed(0); artist.penup()

# TODO:
# 1) Mouse controls drawing (click/drag)
# 2) Keyboard changes colors (e.g., r/g/b/y/p)
# 3) Number keys change brush size
# 4) Space clears screen
screen.exitonclick()
