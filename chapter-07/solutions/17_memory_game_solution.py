import turtle, random, time

screen = turtle.Screen(); screen.setup(400, 400); screen.tracer(0)

# Create 4 pads: up-left (red), up-right (blue), down-left (green), down-right (yellow)
pads = []
def pad(x, y, color):
    t = turtle.Turtle(); t.shape("square"); t.shapesize(3,3); t.color(color); t.penup(); t.goto(x,y)
    pads.append(t); return t

UL = pad(-120, 120, "red")
UR = pad( 120, 120, "blue")
DL = pad(-120,-120, "green")
DR = pad( 120,-120, "yellow")

pad_list = [UL, UR, DL, DR]

sequence = []
player_clicks = []
level = 1
playing = True

def flash(t):
    old = t.color()[0]
    t.color("white"); screen.update(); time.sleep(0.25)
    t.color(old);     screen.update(); time.sleep(0.15)

def on_click(x, y):
    global player_clicks, sequence, level, playing
    # find closest pad
    chosen = min(pad_list, key=lambda p: p.distance(x,y))
    player_clicks.append(chosen)
    flash(chosen)
    # check partial correctness
    idx = len(player_clicks)-1
    if player_clicks[idx] is not sequence[idx]:
        print("Wrong! Game over. Level reached:", level)
        playing = False
        screen.onclick(None)
        return
    # if finished the whole sequence correctly, next round
    if len(player_clicks) == len(sequence):
        level += 1
        print("Good! Level", level-1, "complete")
        screen.onclick(None)  # pause input during playback
        time.sleep(0.5)
        play_round()

def play_round():
    global sequence, player_clicks
    player_clicks = []
    sequence.append(random.choice(pad_list))
    # show sequence
    for p in sequence:
        flash(p)
    # allow clicks
    screen.onclick(on_click)

# start the game
print("Memory Game: watch the flashes, then click pads in order!")
play_round()

# run an idle loop until playing ends
while playing:
    screen.update()
    time.sleep(0.02)

screen.exitonclick()
