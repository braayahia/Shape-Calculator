from shape import Shape
from math import pi

class Circle(Shape):

    def __init__(self, radius) -> None:
        try:
            self.validate_input([radius])
        except TypeError as e:
            print(e)
            exit(1)

        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2
