# Define a class named Shape and its subclass Square. The Square class has an init
# function which takes a length as argument. Both classes have an area function which
# can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length=length
    def area(self):
        return self.length**2
    
shape=Shape()
square_length=Square(float(input("Enter the length of the square:")))
print(f"Shape's are by default:{shape.area()}.")
print(f"Area of the square:{square_length.area()}.")