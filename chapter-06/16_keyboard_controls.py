import turtle

screen = turtle.Screen()
screen.setup(600, 600)

artist = turtle.Turtle()
artist.shape("turtle")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write("Use arrow keys to move the turtle!", align="center", font=("Arial", 16, "bold"))

def move_up():
    artist.setheading(90)
    artist.forward(20)

def move_down():
    artist.setheading(270)
    artist.forward(20)

def move_left():
    artist.setheading(180)
    artist.forward(20)

def move_right():
    artist.setheading(0)
    artist.forward(20)

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.listen()

screen.exitonclick()
