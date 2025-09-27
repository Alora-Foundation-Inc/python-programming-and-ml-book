import turtle

t = turtle.Turtle()
t.write("turtle.done() keeps this window open!", align="center", font=("Arial", 14, "normal"))

turtle.done()  # without this, some setups close immediately after drawing
