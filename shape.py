from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    def validate_input(self, attrs):
        for attr in attrs:
            if attr <= 0:
                raise TypeError("Invalid input! Input value must be positive numbers")

    def __str__(self):
        return f"{self.__class__.__name__}: Area = {self.get_area()}, Perimeter = {self.get_perimeter()}"