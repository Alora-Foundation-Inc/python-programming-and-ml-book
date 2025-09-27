import turtle, time, random

screen = turtle.Screen(); screen.setup(600,600); screen.bgcolor("black"); screen.tracer(0)

score, high_score = 0, 0
score_pen = turtle.Turtle(); score_pen.hideturtle(); score_pen.color("white"); score_pen.penup(); score_pen.goto(0,260)
game_over_pen = turtle.Turtle(); game_over_pen.hideturtle(); game_over_pen.color("red"); game_over_pen.penup()

def update_display():
    score_pen.clear()
    score_pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial",16,"bold"))

def show_game_over():
    game_over_pen.clear()
    game_over_pen.goto(0,20)
    game_over_pen.write("GAME OVER!", align="center", font=("Arial",24,"bold"))
    game_over_pen.goto(0,-20)
    game_over_pen.write("Press R to Restart or Q to Quit", align="center", font=("Arial",14,"normal"))
    screen.update()

update_display(); show_game_over()

def restart():
    global score
    score = 0
    game_over_pen.clear()
    update_display()
    print("Restarted!")

def quit_game(): screen.bye()

screen.onkey(restart, "r"); screen.onkey(quit_game, "q"); screen.listen()
screen.mainloop()
