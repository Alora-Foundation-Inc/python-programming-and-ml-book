# Return two values at once (area and perimeter) and unpack them.

def calculate_rectangle_properties(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

rect_area, rect_perimeter = calculate_rectangle_properties(10, 5)
print(f"Area: {rect_area}, Perimeter: {rect_perimeter}")
