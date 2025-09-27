# Load garden back from the text file.
def load_garden_from_file(filename):
    items = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                kind = parts[0]
                if kind == "flower":
                    items.append({
                        "type": "flower",
                        "x": int(parts[1]), "y": int(parts[2]),
                        "color": parts[3], "petals": int(parts[4])
                    })
                elif kind == "tree":
                    items.append({
                        "type": "tree",
                        "x": int(parts[1]), "y": int(parts[2]),
                        "height": int(parts[5]), "leaf_color": parts[6]
                    })
    except FileNotFoundError:
        print("File not found:", filename)
    return items

loaded = load_garden_from_file("my_garden.txt")
print("Loaded items:", loaded)
