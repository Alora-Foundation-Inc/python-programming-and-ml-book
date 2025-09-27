# Two‑Player Snake — Starter
import turtle, time

screen = turtle.Screen(); screen.setup(800,600); screen.bgcolor("black"); screen.tracer(0)

p1 = turtle.Turtle(); p1.shape("square"); p1.color("red");  p1.penup(); p1.goto(-100,0); p1.direction="right"
p2 = turtle.Turtle(); p2.shape("square"); p2.color("blue"); p2.penup(); p2.goto( 100,0); p2.direction="left"

# TODO:
# - WASD controls for P1, arrow keys for P2
# - Each grows when eating food (shared or separate)
# - End game when either hits wall, self, or the other snake
screen.exitonclick()
