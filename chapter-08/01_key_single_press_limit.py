import turtle

screen = turtle.Screen()
player = turtle.Turtle(); player.shape("square")

def move_up(): player.sety(player.ycor()+20)

# Only handles one key at a time, and feels jumpy
screen.onkey(move_up, "Up")
screen.listen()

print("Press Up a bunch. Notice it's tap-based, not smooth, and only one key at a time.")
screen.exitonclick()
