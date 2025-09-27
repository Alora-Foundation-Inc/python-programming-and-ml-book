# Ultimate Snake Starter — fill in TODOs
import turtle, time, random

# Screen
screen = turtle.Screen(); screen.setup(600,600); screen.bgcolor("black"); screen.tracer(0); screen.title("Ultimate Snake — Starter")

# Head, food, segments
head = turtle.Turtle(); head.shape("square"); head.color("lime"); head.penup(); head.goto(0,0); head.direction="right"
food = turtle.Turtle(); food.shape("circle"); food.color("red"); food.penup()
segments = []

# State
score = 0; high_score = 0; level = 1; food_eaten = 0; game_over = False; paused = False
food_type = "normal"

# Pens
score_pen = turtle.Turtle(); score_pen.hideturtle(); score_pen.color("white"); score_pen.penup(); score_pen.goto(0,260)
game_over_pen = turtle.Turtle(); game_over_pen.hideturtle(); game_over_pen.color("red"); game_over_pen.penup()

# TODO:
# - write update_display(), calculate_speed(), place_food() (10% special gold triangle), add_segment()
# - write move(), check_food(), check_collisions() (wall + self using segments[2:])
# - write show_game_over(), restart_game(), toggle_pause()
# - bind keys: arrows to move, 'r' restart, 'q' quit, space pause
# - main loop: if not game_over and not paused -> move, check collisions & food, sleep
#   else sleep a tiny bit

screen.mainloop()
