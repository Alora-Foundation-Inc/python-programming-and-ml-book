# Track score, lives, level in a dictionary.
import turtle

game_state = {"score": 0, "lives": 3, "level": 1, "playing": True}

screen = turtle.Screen()
player = turtle.Turtle(); player.shape("turtle")

def show_game_info():
    print(f"Score: {game_state['score']}")
    print(f"Lives: {game_state['lives']}")
    print(f"Level: {game_state['level']}")

def player_hit():
    game_state["lives"] -= 1
    print("Hit! Lives remaining:", game_state["lives"])
    if game_state["lives"] <= 0:
        game_state["playing"] = False
        print("Game Over!")

def score_point():
    game_state["score"] += 10
    print("Score:", game_state["score"])
    if game_state["score"] % 50 == 0:
        game_state["level"] += 1
        print("Level up! Now level", game_state["level"])

show_game_info()
for _ in range(5): score_point()  # demos a level up at 50
player_hit()
show_game_info()

screen.exitonclick()
