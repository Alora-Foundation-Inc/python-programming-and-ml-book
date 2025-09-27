import turtle

screen = turtle.Screen(); screen.setup(500, 400)
player = turtle.Turtle(); player.shape("turtle"); player.color("green")

def goto_mouse(x, y): player.goto(x, y)
# def follow_mouse(x, y): player.setheading(player.towards(x,y)); player.goto(x,y)

screen.onclick(goto_mouse)
print("Click anywhere to move the turtle! (Try changing to follow mode)")
screen.exitonclick()
