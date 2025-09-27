import turtle

screen = turtle.Screen()
screen.title("Collision Test")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = turtle.Turtle()
snake.speed(0); snake.shape("square"); snake.color("green"); snake.penup(); snake.goto(0,0)

food = turtle.Turtle()
food.speed(0); food.shape("circle"); food.color("red"); food.penup(); food.goto(40,0)

def check_collision():
    distance = snake.distance(food)
    print(f"Distance between snake and food: {distance}")
    if distance < 20:
        print("Snake ate the food!")
        food.color("yellow")
        return True
    return False

snake.goto(20,0); screen.update(); check_collision()
snake.goto(40,0); screen.update(); check_collision()

screen.exitonclick()
