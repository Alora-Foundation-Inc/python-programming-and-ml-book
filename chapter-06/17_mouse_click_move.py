import turtle

screen = turtle.Screen()
screen.setup(600, 600)

artist = turtle.Turtle()

def goto_click(x, y):
    artist.goto(x, y)

# Try changing to draw_at_click to draw small circles
# def draw_at_click(x, y):
#     artist.goto(x, y)
#     artist.circle(20)

screen.onclick(goto_click)
print("Click anywhere to move the turtle!")

screen.exitonclick()
