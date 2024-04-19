from shape import Shape

class Hexagon(Shape):
    def __init__(self, size):
        try:
            self.validate_input([size])
        except TypeError as e:
            print(e)
            exit(1)
            
        self.size = size
        
    def get_name(self):
        return "Hexagon"
        
    def get_area(self):
        from math import sqrt
        return 3 * sqrt(3) * self.size ** 2 / 2