# Turtle bar chart: Student heights
import turtle

screen = turtle.Screen()
screen.setup(600, 400)
screen.bgcolor("white")
t = turtle.Turtle(); t.speed(0)

names  = ["Alex", "Ben", "Cara", "Dana", "Eli"]
heights= [58, 62, 55, 60, 64]   # inches

start_x = -200
bar_w = 60

for i, name in enumerate(names):
    x = start_x + i*80
    h = heights[i]*2  # scale
    t.penup(); t.goto(x, 0); t.pendown()
    t.begin_fill()
    # draw rectangle (bar)
    t.forward(bar_w); t.left(90); t.forward(h)
    t.left(90); t.forward(bar_w); t.left(90); t.forward(h)
    t.left(90); t.end_fill()
    # labels
    t.penup(); t.goto(x + bar_w/2, -20)
    t.write(name, align="center", font=("Arial", 10, "normal"))
    t.goto(x + bar_w/2, h + 5)
    t.write(f"{heights[i]}"", align="center", font=("Arial", 9, "normal"))
t.hideturtle()
print("Student Heights Bar Chart (Turtle)")
screen.exitonclick()
