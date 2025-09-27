import turtle, time

screen = turtle.Screen()
screen.title("Growing Snake Movement")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0); head.shape("square"); head.color("green"); head.penup(); head.goto(0,0); head.direction = "right"

segments = []

def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0); new_segment.shape("square"); new_segment.color("lightgreen"); new_segment.penup()
    segments.append(new_segment)

def move():
    for i in range(len(segments)-1, 0, -1):
        x, y = segments[i-1].xcor(), segments[i-1].ycor()
        segments[i].goto(x, y)
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    if head.direction == "up": head.sety(head.ycor()+20)
    elif head.direction == "down": head.sety(head.ycor()-20)
    elif head.direction == "left": head.setx(head.xcor()-20)
    elif head.direction == "right": head.setx(head.xcor()+20)

add_segment(); add_segment()
print("Watch the snake move and grow! Starting with 2 body segments")
for i in range(15):
    move(); screen.update(); time.sleep(0.3)
    if (i+1) % 5 == 0:
        add_segment()
        print(f"Snake grew! Now has {len(segments)} segments")

screen.exitonclick()
