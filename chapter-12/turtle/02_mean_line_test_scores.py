# Turtle mean line demo using a simple horizontal marker
import turtle

scores = [85, 92, 78, 88, 95, 82, 90]
mean = sum(scores)/len(scores)

screen = turtle.Screen(); screen.setup(700, 400); screen.bgcolor("white"); screen.title("Mean Line (Turtle)")
pen = turtle.Turtle(); pen.speed(0); pen.hideturtle()

# axis baseline
pen.penup(); pen.goto(-300, -120); pen.pendown(); pen.forward(600)

# map score (60..100) roughly to y (-80..180)
def y_from_score(s):
    return -80 + (s - 60) * (260/40)

# plot points S1..Sn
x = -250
for i, s in enumerate(scores):
    pen.penup(); pen.goto(x + i*80, y_from_score(s)); pen.dot(12)
    pen.goto(x + i*80, -110); pen.write(f"S{i+1}", align="center", font=("Arial", 9, "normal"))

# draw mean line
pen.color("red")
pen.penup(); pen.goto(-280, y_from_score(mean))
pen.pendown(); pen.forward(560)
pen.penup(); pen.goto(-280, y_from_score(mean)+8)
pen.write(f"Mean ≈ {mean:.1f}", font=("Arial", 10, "bold"))
print("Mean line drawn. Close the window to finish.")
screen.exitonclick()
