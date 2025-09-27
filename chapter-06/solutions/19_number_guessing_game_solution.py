import random, turtle

secret = random.randint(1, 10)
won = False

for guess_num in range(1, 4):
    try:
        g = int(input(f"Guess #{guess_num}: "))
    except ValueError:
        print("Please enter a number 1..10")
        continue

    if g < secret:
        print("Too low!")
    elif g > secret:
        print("Too high!")
    else:
        print("You got it!")
        won = True
        break

if won:
    t = turtle.Turtle()
    for _ in range(5):
        t.forward(100); t.right(144)
    turtle.done()
else:
    print("Out of guesses! The number was", secret)
