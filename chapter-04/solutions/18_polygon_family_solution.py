import turtle
t = turtle.Turtle()
t.speed(8)

def draw_polygon(sides, size, color):
    t.color(color)
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)

def triangle(size, color): return draw_polygon(3, size, color)
def square(size, color):   return draw_polygon(4, size, color)
def pentagon(size, color): return draw_polygon(5, size, color)
def hexagon(size, color):  return draw_polygon(6, size, color)

triangle(80, "red")
t.penup(); t.goto(120, 0); t.pendown()
square(80, "blue")
t.penup(); t.goto(-120, 0); t.pendown()
hexagon(60, "green")

turtle.done()
