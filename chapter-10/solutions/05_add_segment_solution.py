import turtle

screen = turtle.Screen()
screen.title("Snake Growth Test")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0); head.shape("square"); head.color("green"); head.penup(); head.goto(0,0)

segments = []

def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0); new_segment.shape("square"); new_segment.color("lightgreen"); new_segment.penup()
    segments.append(new_segment)
    print(f"Snake now has {len(segments)} body segments")

for i in range(5):
    add_segment()
    for j, seg in enumerate(segments):
        seg.goto(-20*(j+1), 0)
    screen.update()
    input("Press Enter to add another segment...")

screen.exitonclick()
