# Guess a random number 1..10 with up to 3 tries.
import random

secret = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10. You have 3 guesses!")

# TODO:
# - Loop up to 3 times
# - Use try/except to convert input to int
# - Print "Too low!" / "Too high!" or "You got it!"
# - (Optional) Draw a turtle star when winning
