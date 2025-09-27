# Multi-food: keep 3-5 food items on screen, respawn when eaten.
import turtle, random, time

screen = turtle.Screen(); screen.setup(600,600); screen.bgcolor("black"); screen.tracer(0)

head = turtle.Turtle(); head.shape("square"); head.color("green"); head.penup(); head.direction="right"

foods = []  # list of food turtles

# TODO:
# 1) Create 3-5 food turtles with different colors
# 2) Place them at random grid spots
# 3) In a loop, move the head and check all foods:
#    if head.distance(food) < 20 -> increment score and move that food somewhere else
screen.exitonclick()
