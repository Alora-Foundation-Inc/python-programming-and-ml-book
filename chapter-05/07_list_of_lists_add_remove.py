flowers = [
    [50, 100, "red", 6],
    [150, 50, "blue", 8],
    [-100, 75, "yellow", 5]
]
print("Start:", flowers)

flowers.append([0, -50, "purple", 7])
print("After append:", flowers)

removed = flowers.pop(0)  # remove first
print("Popped:", removed)
print("Now:", flowers)

flowers.remove([150, 50, "blue", 8])  # remove exact match
print("After remove exact:", flowers)
