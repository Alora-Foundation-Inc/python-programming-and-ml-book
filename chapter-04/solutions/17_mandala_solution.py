import turtle

t = turtle.Turtle()
t.speed(0)

def draw_mandala(spokes=12, radius=80, color_list=None):
    if color_list is None:
        color_list = ["red","orange","yellow","green","blue","purple"]
    angle = 360 / spokes
    for i in range(spokes):
        t.color(color_list[i % len(color_list)])
        t.penup(); t.goto(0,0); t.pendown()
        t.setheading(i * angle)
        t.forward(radius)
        # tiny motif at the end of the spoke
        t.right(30); t.forward(20); t.backward(20)
        t.left(60); t.forward(20); t.backward(20)

draw_mandala(18, 100)
turtle.done()
