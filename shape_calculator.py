import math


# Class that represents a rectangle and its associated properties
class Rectangle:

    # Constructor method
    def __init__(self, width=1, height=1):
        self._width = width
        self._height = height

    # Get method for height
    def get_height(self):
        return self._height

    # Set method for height
    def set_height(self, h):
        self._height = h

    # Get method for width
    def get_width(self):
        return self._width

    # Set method for width
    def set_width(self, w):
        self._width = w

    # Returns string representation of Rectangle obj
    def __repr__(self):
        return f'Rectangle(width={self.get_width()}, height={self.get_height()})'

    # Compute area
    def get_area(self):
        return self.get_width() * self.get_height()

    # Compute perimeter
    def get_perimeter(self):
        return 2 * (self.get_width() + self.get_height())

    # Compute diagonal length
    def get_diagonal(self):
        return (self.get_width() ** 2 + self.get_height() ** 2) ** .5

    # Returns a string that represents the shape using lines of "*".
    def get_picture(self):
        result = list()
        for i in range(self.get_height()):
            result.append("*" * self.get_width() + "\n")

        # Concatenate elements in list into single string
        result = ''.join(result)

        if self.get_height() > 50 or self.get_width() > 50:
            return "Too big for picture."

        return result

    # Returns the number of times the passed in shape could fit inside the shape (with no rotations).
    def get_amount_inside(self, other):
        return math.floor(self.get_area() / other.get_area())


# Class that represents a square and its associated properties
class Square(Rectangle):

    # Constructor method
    def __init__(self, side=1):
        super().__init__(width=side, height=side)
        self._side = side

    # Set method for side
    def get_side(self):
        return self._side

    # Method to set side
    def set_side(self, s):
        self._side = s

    # Returns a string that represents the shape using lines of "*".
    def get_picture(self):
        result = list()
        for i in range(self.get_side()):
            result.append("*" * self.get_side() + "\n")

        # Concatenate elements in list into single string
        result = ''.join(result)

        if self.get_height() > 50 or self.get_width() > 50:
            return "Too big for picture."

        return result

    # Returns string representation of Square obj
    def __repr__(self):
        return f'Square(side={self.get_side()})'
