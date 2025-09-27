# Special food types with different effects.
# Red (circle): +10 points, +1 segment
# Blue (square): +20 points, +2 segments
# Yellow (triangle): +50 points, +0 segments
# Purple (star): +100 points, +3 segments (rare)
import turtle, random, time

screen = turtle.Screen(); screen.setup(600,600); screen.bgcolor("black"); screen.tracer(0)
head = turtle.Turtle(); head.shape("square"); head.color("green"); head.penup(); head.direction="right"

# TODO:
# - Make different food turtles + shapes/colors
# - When eaten, apply the effect to score/growth
# - Respawn that food somewhere random
screen.exitonclick()
