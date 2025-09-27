import turtle
t = turtle.Turtle()
t.speed(7)

for i in range(200):
    t.forward(i * 3 / 2)
    t.right(90)
    x, y = t.position()
    if abs(x) > 200 or abs(y) > 200:
        print("Spiral got too big! Stopping early.")
        break

print("Loop finished!")
turtle.done()
