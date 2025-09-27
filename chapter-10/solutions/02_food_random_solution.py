import turtle, random

screen = turtle.Screen()
screen.title("Snake Game - Random Food")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()

def place_food_randomly():
    x = random.randint(-14, 14) * 20
    y = random.randint(-14, 14) * 20
    food.goto(x, y)
    print(f"Food placed at ({x}, {y})")

for i in range(5):
    place_food_randomly()
    screen.update()
    input("Press Enter for next food location...")

screen.exitonclick()
