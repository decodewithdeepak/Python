# Write python program to calculate area and perimeter of different shapes using polymorphism.

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):  # Square is a special case of Rectangle
    def __init__(self, side):
        super().__init__(side, side)

# Example usage:
circle = Circle(5)
print(f"Circle - Area: {circle.area()}, Perimeter: {circle.perimeter()}")

rectangle = Rectangle(4, 6)
print(f"Rectangle - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")

square = Square(3)
print(f"Square - Area: {square.area()}, Perimeter: {square.perimeter()}")
