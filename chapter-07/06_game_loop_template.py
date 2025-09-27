import turtle, time

screen = turtle.Screen()
screen.tracer(0)

player = turtle.Turtle()
player.shape("square"); player.color("blue")

game_running = True
frame_count = 0

while game_running:
    # 1) handle input (key handlers would run automatically)
    # 2) update world
    frame_count += 1
    # 3) draw
    screen.update()
    # 4) control frame rate
    time.sleep(0.02)
    if frame_count > 250:  # ~5 seconds
        game_running = False

print("Game finished!")
screen.exitonclick()
