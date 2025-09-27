def safe_save_data(data, filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for item in data:
                f.write(str(item) + "\n")
        print("Saved to", filename)
        return True
    except IOError:
        print("Error: Could not save to", filename)
        return False

def safe_load_data(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
        print("Loaded from", filename)
        return lines
    except FileNotFoundError:
        print("Error: File not found", filename)
        return []
    except IOError:
        print("Error: Could not read", filename)
        return []

test_data = ["flower,50,100,red,6", "tree,0,-50,100,green"]
safe_save_data(test_data, "test_garden.txt")
print("Loaded:", safe_load_data("test_garden.txt"))
