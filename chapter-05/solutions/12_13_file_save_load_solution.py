def save_garden(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        for item in data:
            line = f"{item['type']},{item['x']},{item['y']},"                    f"{item.get('color','')},{item.get('petals','')},"                    f"{item.get('height','')},{item.get('leaf_color','')}
"
            f.write(line)

def load_garden(filename):
    result = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            kind = parts[0]
            if kind == "flower":
                result.append({"type":"flower","x":int(parts[1]),"y":int(parts[2]),"color":parts[3],"petals":int(parts[4])})
            elif kind == "tree":
                result.append({"type":"tree","x":int(parts[1]),"y":int(parts[2]),"height":int(parts[5]),"leaf_color":parts[6]})
    return result

garden = [
    {"type":"flower","x":50,"y":100,"color":"red","petals":6},
    {"type":"tree","x":0,"y":-50,"height":120,"leaf_color":"green"}
]

save_garden("garden_demo.txt", garden)
loaded = load_garden("garden_demo.txt")
print("Loaded:", loaded)
