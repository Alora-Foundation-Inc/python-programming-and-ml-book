# Solution: 3x3 Pattern Grid (each cell a tiny motif)
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

cell = 120
start_x, start_y = -cell, cell  # top-left cell

def draw_square(size):
    for _ in range(4):
        t.forward(size); t.right(90)

def draw_triangle(size):
    for _ in range(3):
        t.forward(size); t.left(120)

def draw_star(size):
    for _ in range(5):
        t.forward(size); t.right(144)

motifs = [
    lambda: draw_square(60),
    lambda: draw_triangle(70),
    lambda: draw_star(60),
    lambda: [t.circle(30), t.right(30)],
    lambda: [draw_square(40), t.penup(), t.forward(10), t.pendown(), draw_square(20)],
    lambda: [t.color("purple"), t.circle(20, 180), t.left(90), t.circle(20, 180), t.color("black")],
    lambda: [t.forward(50), t.backward(100), t.forward(50), t.left(90), t.forward(50), t.backward(100), t.forward(50), t.right(90)],
    lambda: [t.pensize(4), draw_triangle(40), t.pensize(2)],
    lambda: [t.color("blue"), draw_star(40), t.color("black")]
]

idx = 0
for row in range(3):
    for col in range(3):
        # move to cell origin
        t.penup(); t.goto(start_x + col*cell, start_y - row*cell); t.pendown()
        # draw cell boundary (optional)
        t.color("#cccccc"); draw_square(cell-10); t.color("black")
        # move inside and draw motif
        t.penup(); t.forward(30); t.right(90); t.forward(30); t.left(90); t.pendown()
        # draw motif
        m = motifs[idx % len(motifs)]
        m()
        idx += 1

turtle.done()
