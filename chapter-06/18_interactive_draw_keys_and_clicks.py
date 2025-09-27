import turtle

screen = turtle.Screen()
screen.setup(600, 600)

artist = turtle.Turtle()
artist.shape("turtle")

def move_up():    artist.setheading(90);  artist.forward(10)
def move_down():  artist.setheading(270); artist.forward(10)
def move_left():  artist.setheading(180); artist.forward(10)
def move_right(): artist.setheading(0);   artist.forward(10)

def draw_at_click(x, y):
    artist.goto(x, y)
    artist.dot(10)

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onclick(draw_at_click)
screen.listen()

print("Arrow keys to move, click to draw dots!")
screen.exitonclick()
