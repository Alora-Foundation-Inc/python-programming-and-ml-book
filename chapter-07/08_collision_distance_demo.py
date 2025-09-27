import turtle

object1 = turtle.Turtle(); object1.shape("circle"); object1.color("red"); object1.goto(-100, 0)
object2 = turtle.Turtle(); object2.shape("circle"); object2.color("blue"); object2.goto(100, 0)

distance = object1.distance(object2)
print("Distance:", distance)

if distance < 40:
    print("Collision detected!")
else:
    print("No collision")

turtle.done()
