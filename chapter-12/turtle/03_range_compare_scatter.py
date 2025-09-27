# Turtle comparison of spread (range) for two classes
import turtle

class_a = [75, 77, 78, 79, 80, 81, 82, 83, 85]
class_b = [60, 65, 75, 80, 85, 85, 90, 95, 100]

screen = turtle.Screen(); screen.setup(800, 500); screen.bgcolor("white"); screen.title("Range Comparison (Turtle)")
pen = turtle.Turtle(); pen.speed(0); pen.hideturtle()

def y_from_score(s): return -180 + (s - 50) * (360/60)

# Draw points for Class A (left) and B (right)
for i, s in enumerate(class_a):
    pen.penup(); pen.goto(-200 + i*20, y_from_score(s)); pen.dot(10)

for i, s in enumerate(class_b):
    pen.penup(); pen.goto(100 + i*20, y_from_score(s)); pen.dot(10)

# draw approximate min/max lines
def draw_min_max(x_left, n, series):
    pen.penup(); pen.goto(x_left, y_from_score(min(series))); pen.pendown(); pen.forward(n*20)
    pen.penup(); pen.goto(x_left, y_from_score(max(series))); pen.pendown(); pen.forward(n*20)

draw_min_max(-200, len(class_a), class_a)
draw_min_max(100, len(class_b), class_b)

pen.penup(); pen.goto(-200, 200); pen.write("Class A", font=("Arial", 12, "bold"))
pen.goto(100, 200); pen.write("Class B", font=("Arial", 12, "bold"))
screen.exitonclick()
