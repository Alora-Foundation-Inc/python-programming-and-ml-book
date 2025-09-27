import turtle
t = turtle.Turtle()
t.speed(6)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(30):
    if i % 5 == 0:
        continue              # skip multiples of 5
    if i > 20:
        print("That's enough drawing!")
        break                 # stop early

    t.color(colors[i % len(colors)])
    t.forward(i * 5)
    t.right(60)

turtle.done()
