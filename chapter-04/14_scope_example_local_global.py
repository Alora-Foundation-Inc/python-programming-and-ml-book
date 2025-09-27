import turtle

my_turtle = turtle.Turtle()
size = 100  # global

def draw_square():
    size = 50  # local shadows the global inside this function
    for _ in range(4):
        my_turtle.forward(size)
        my_turtle.right(90)

draw_square()
print(f"Size is: {size}")  # prints 100

turtle.done()
