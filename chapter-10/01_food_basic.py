import turtle

screen = turtle.Screen()
screen.title("Snake Game - Food Test")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

print("Food created at (0, 100)")
screen.update()
screen.exitonclick()
