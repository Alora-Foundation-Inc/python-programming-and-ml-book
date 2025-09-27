import turtle

screen = turtle.Screen()
artist = turtle.Turtle()

answer = input("Do you want a circle? (yes/no): ")

if not answer == "no":
    artist.circle(40)
    print("Here's your circle!")
else:
    print("No circle for you!")

screen.exitonclick()
