# Save garden to a simple CSV-like text file.
garden_data = [
    {"type": "flower", "x": 50, "y": 100, "color": "red",  "petals": 6},
    {"type": "flower", "x":-50, "y":  50, "color": "blue", "petals": 8},
    {"type": "tree",   "x": 0,  "y": -50, "height": 100, "leaf_color": "green"}
]

with open("my_garden.txt", "w", encoding="utf-8") as f:
    for item in garden_data:
        line = f"{item['type']},{item['x']},{item['y']},"                f"{item.get('color','')},{item.get('petals','')},"                f"{item.get('height','')},{item.get('leaf_color','')}
"
        f.write(line)

print("Garden data saved to my_garden.txt")
