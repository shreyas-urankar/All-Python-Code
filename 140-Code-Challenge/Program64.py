# Given the side length x find the area of a hexagon.
# Examples
# area_of_hexagon(1) ➞ 2.6
# area_of_hexagon(2) ➞ 10.4
# area_of_hexagon(3) ➞ 23.4

# import math
# def area_of_Hexagon(x):
#     area=(3*math.sqrt(3)*x**2)/2
#     return round(area,1)

# print(area_of_Hexagon(1))
# print(area_of_Hexagon(2))
import math
class Hexagon:
    def __init__(self,x) -> None:
        self.x=x
    def area(self):
        area=(3 * math.sqrt(3) * self.x**2) / 2
        return round(area, 1)
    
x=int(input("Enter the side of hexagon (x):"))
h=Hexagon(x)
hexagon_area=h.area()
print(f"The are of hexagon is: {hexagon_area}")
