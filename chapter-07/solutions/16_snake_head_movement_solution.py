import turtle, time

screen = turtle.Screen(); screen.setup(600, 400); screen.tracer(0)

head = turtle.Turtle(); head.shape("square"); head.color("lime"); head.penup()
head.setheading(0)
step = 8
running = True

def up():    head.setheading(90)
def down():  head.setheading(270)
def left_(): head.setheading(180)
def right_():head.setheading(0)

screen.onkey(up,"Up"); screen.onkey(down,"Down"); screen.onkey(left_,"Left"); screen.onkey(right_,"Right"); screen.listen()

while running:
    head.forward(step)
    x, y = head.xcor(), head.ycor()
    if x > 290 or x < -290 or y > 190 or y < -190:
        running = False
    screen.update(); time.sleep(0.05)

print("Stopped at wall!")
screen.exitonclick()
