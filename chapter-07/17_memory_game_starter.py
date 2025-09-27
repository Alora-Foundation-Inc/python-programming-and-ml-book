# Simple Simon-style memory: flash colored squares, click to repeat.
import turtle, random, time

screen = turtle.Screen()
screen.setup(400, 400)

# TODO:
# 1. Make 4 colored squares (turtles) at corners
# 2. Build a sequence list; flash turtles in order (change color briefly)
# 3. On clicks, record player's choices and compare to sequence
# 4. If correct, extend sequence; if wrong, game over
screen.exitonclick()
