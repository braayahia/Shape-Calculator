from rectangle import Rectangle

class Triangle(Rectangle):

  def __init__(self, base, height):
    super().__init__(base, height)

  def get_area(self):
    return 0.5 * super().get_area()