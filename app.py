from hexagon import Hexagon
from rectangle import Rectangle
from square import Square
from circle import Circle
from triangle import Triangle

class App():
    def __init__(self):
        self.menu()
    
    def menu(self):
        print("Hello there, select a shape from the menu")
        print("1) rectangle")
        print("2) square")
        print("3) triangle")
        print("4) circle")
        print("5) hexagon")
        print("Enter nothing to exit")
        self.input_handler()
        
        
    def input_handler(self):
        selected_shape = input("")
        if selected_shape == "1":
            width = int(input("Please enter rectangle's width:\n"))
            height = int(input("Please enter rectangle's height:\n"))
            rec = Rectangle(width, height)
            print(rec.get_area())
        if selected_shape == "2":
            side = int(input("Please enter square's side:\n"))
            sq = Square(side)
            print(sq.get_area())
        if selected_shape == "3":
            base = int(input("Please enter triangle's base:\n"))
            height = int(input("Please enter ttriangle's height:\n"))
            tri = Triangle(base, height)
            print(tri.get_area())
        if selected_shape == "4":
            radius = int(input("Please enter circle's radius:\n"))
            cr = Circle(radius)
            print(cr.get_area())
        if selected_shape == "5":
            lengths = int(input("Please enter hexagon's size:\n"))
            hex = Hexagon(lengths)
            print(hex.get_area())
