colors = ["red", "blue", "green"]
print("Start:", colors)

colors.append("yellow")
colors.append("purple")
print("After append:", colors)

colors.insert(1, "orange")
print("After insert:", colors)

colors.remove("blue")
print("After remove 'blue':", colors)

length = len(colors)
print("Length:", length)

has_red = "red" in colors
has_pink = "pink" in colors
print("Has red:", has_red)
print("Has pink:", has_pink)
