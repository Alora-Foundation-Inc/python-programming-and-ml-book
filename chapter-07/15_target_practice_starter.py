# Click targets before they disappear.
import turtle, random, time

screen = turtle.Screen()
screen.setup(600, 400)

score = 0
targets = []

def make_target():
    t = turtle.Turtle(); t.shape("circle"); t.color("red"); t.penup()
    t.goto(random.randint(-280, 280), random.randint(-180, 180))
    t.onclick(hit_target)  # when clicked, call hit_target
    targets.append(t)

def hit_target(x, y):
    global score
    score += 1
    print("Hit! Score:", score)

# TODO:
# - loop for a time limit
# - spawn targets sometimes, remove old ones
# - end and print final score
screen.exitonclick()
