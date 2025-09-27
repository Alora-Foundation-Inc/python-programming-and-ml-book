import turtle
t = turtle.Turtle()
t.speed(6)

for i in range(5):              # 0,1,2,3,4  → 5 steps
    print(f"Step {i}")
    t.forward(50)
    t.right(72)                 # 360/5

turtle.done()
