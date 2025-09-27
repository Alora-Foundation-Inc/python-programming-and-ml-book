import turtle
my_turtle = turtle.Turtle(); my_turtle.speed(7)

def move_to(x, y): my_turtle.penup(); my_turtle.goto(x, y); my_turtle.pendown()

garden = {
    "weather": {"rain": True, "sun": False, "temp": 20},
    "plants": [
        {"type":"flower", "x":-120, "y":90, "needs":{"water":True,"sun":True,"temp_min":15}},
        {"type":"fern",   "x":-20,  "y":40, "needs":{"water":True,"sun":False,"temp_min":10}},
        {"type":"cactus", "x":120,  "y":-40,"needs":{"water":False,"sun":True,"temp_min":5}},
    ]
}

def healthy(p, w):
    need = p["needs"]
    ok_water = (not need["water"]) or w["rain"]
    ok_sun   = (not need["sun"])   or w["sun"]
    ok_temp  = w["temp"] >= need["temp_min"]
    return ok_water and ok_sun and ok_temp

def draw(kind, is_ok):
    if kind=="flower":
        my_turtle.color("red" if is_ok else "brown")
        for _ in range(6):
            my_turtle.circle(15,60); my_turtle.left(120)
            my_turtle.circle(15,60); my_turtle.left(120); my_turtle.right(60)
    elif kind=="fern":
        my_turtle.color("green" if is_ok else "brown")
        for _ in range(4): my_turtle.forward(30); my_turtle.backward(30); my_turtle.right(90)
    elif kind=="cactus":
        my_turtle.color("green" if is_ok else "yellow")
        my_turtle.left(90); my_turtle.forward(40); my_turtle.backward(40); my_turtle.right(90)

for p in garden["plants"]:
    move_to(p["x"], p["y"])
    draw(p["type"], healthy(p, garden["weather"]))

# save
with open("smart_garden.txt","w",encoding="utf-8") as f:
    f.write(str(garden))

# load (simple eval-free parse: very basic demonstration)
loaded_str = open("smart_garden.txt","r",encoding="utf-8").read()
print("Saved garden text length:", len(loaded_str))

turtle.done()
