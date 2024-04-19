# Implementing the Square class in a self-contained environment, inheriting from the Rectangle class.
# To do this, I'll need to define the Rectangle class first for context.
from rectangle import Rectangle



class Square(Rectangle):
    """
    A class representing a square, which is a special kind of rectangle.
    """

    def __init__(self, side_length):
        """
        Initialize a square with all sides of equal length.
        """
        super().__init__(side_length, side_length)  # A square is a rectangle with equal width and length.

    def __repr__(self):
        return f"Square(side_length={self.length})"
