import turtle
my_turtle = turtle.Turtle(); my_turtle.speed(8)

def move_to(x, y): my_turtle.penup(); my_turtle.goto(x, y); my_turtle.pendown()
def star(size):
    for _ in range(5): my_turtle.forward(size); my_turtle.right(144)
def circle_(size): my_turtle.circle(size)
def square(size):
    for _ in range(4): my_turtle.forward(size); my_turtle.right(90)

art = [
    {"type":"star","x":0,"y":100,"size":50,"color":"gold"},
    {"type":"circle","x":120,"y":0,"size":40,"color":"blue"},
    {"type":"square","x":-120,"y":0,"size":60,"color":"green"}
]

# draw
for a in art:
    move_to(a["x"], a["y"]); my_turtle.color(a["color"])
    if a["type"]=="star": star(a["size"])
    elif a["type"]=="circle": circle_(a["size"])
    elif a["type"]=="square": square(a["size"])

# save
with open("art_collection.txt","w",encoding="utf-8") as f:
    for a in art:
        f.write(f"{a['type']},{a['x']},{a['y']},{a['size']},{a['color']}\n")

# load
loaded=[]
with open("art_collection.txt","r",encoding="utf-8") as f:
    for line in f:
        kind,x,y,size,color=line.strip().split(",")
        loaded.append({"type":kind,"x":int(x),"y":int(y),"size":int(size),"color":color})
print("Loaded art:", loaded)

turtle.done()
