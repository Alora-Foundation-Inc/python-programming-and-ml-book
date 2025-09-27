import turtle
t = turtle.Turtle()
t.speed(9)

petals_per_flower = 6
number_of_flowers = 8
palette = ["red", "pink", "yellow", "orange", "purple", "blue", "green", "magenta"]

for flower in range(number_of_flowers):
    t.color(palette[flower % len(palette)])
    # draw petals
    for _ in range(petals_per_flower):
        t.circle(30, 60)
        t.left(120)
        t.circle(30, 60)
        t.left(120)
        t.right(360 / petals_per_flower)
    # rotate to next flower
    t.right(360 / number_of_flowers)

turtle.done()
