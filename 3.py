"""

#question
Write a Python program to create a class named Rectangle with attributes length and
width. Implement methods to calculate the area and perimeter of the rectangle. Also,
implement a method to compare two rectangles based on their area.

"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def compare_area(self, other_rectangle):
        area1 = self.calculate_area()
        area2 = other_rectangle.calculate_area()
        if area1 > area2:
            return "Rectangle 1 is larger."
        elif area1 < area2:
            return "Rectangle 2 is larger."
        else:
            return "Both rectangles have the same area."

rectangle1 = Rectangle(5, 4)
rectangle2 = Rectangle(3, 6)

print("Rectangle 1:")
print(f"Area: {rectangle1.calculate_area()}")
print(f"Perimeter: {rectangle1.calculate_perimeter()}")

print("\nRectangle 2:")
print(f"Area: {rectangle2.calculate_area()}")
print(f"Perimeter: {rectangle2.calculate_perimeter()}")

comparison_result = rectangle1.compare_area(rectangle2)
print("\nComparison Result:")
print(comparison_result)
