import turtle, time

screen = turtle.Screen(); screen.setup(400,300); screen.tracer(0)
game_over = False
t = turtle.Turtle(); t.hideturtle(); t.penup(); t.goto(0,0)

frames = 0
while not game_over:
    frames += 1
    t.clear(); t.write(f"Running... frame {frames}", align="center", font=("Arial",14,"normal"))
    screen.update(); time.sleep(0.05)
    if frames == 100:
        game_over = True

t.clear(); t.write("Game Over — loop stopped", align="center", font=("Arial",16,"bold"))
screen.update()
screen.exitonclick()
