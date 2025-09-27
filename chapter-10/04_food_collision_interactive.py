import turtle, random

screen = turtle.Screen()
screen.title("Snake Food Collision")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = turtle.Turtle()
snake.speed(0); snake.shape("square"); snake.color("green"); snake.penup(); snake.goto(0,0)

food = turtle.Turtle()
food.speed(0); food.shape("circle"); food.color("red"); food.penup()

def place_food():
    x = random.randint(-14, 14) * 20
    y = random.randint(-14, 14) * 20
    food.goto(x, y)

def check_food_collision():
    if snake.distance(food) < 20:
        print("Food eaten!")
        place_food()
        return True
    return False

def move_up():    snake.sety(snake.ycor()+20); check_food_collision()
def move_down():  snake.sety(snake.ycor()-20); check_food_collision()
def move_left():  snake.setx(snake.xcor()-20); check_food_collision()
def move_right(): snake.setx(snake.xcor()+20); check_food_collision()

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

place_food()
print("Use arrow keys to move snake and eat the red food!")
screen.update()
screen.exitonclick()
