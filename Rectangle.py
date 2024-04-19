from shape import Shape

class Rectangle(Shape):

  def __init__(self, width, height):
    try:
      self.validate_input([width, height])
    except TypeError as e:
      print(e)
      exit(1)
    
    self.width = width
    self.height = height
    
  def get_area(self):
    return self.width * self.height