# Create a function that takes the height and radius of a cone as arguments and returns
# the volume of the cone rounded to the nearest hundredth. See the resources tab for
# the formula (Take user input).

import math
def volume_cone():
    radius=float(input("Enter the radius of the cone:"))
    if radius==0:
        return 0
    height=float(input("Enter the height of the cone:"))
    volume=(1/3)*math.pi*(radius**2)*height
    return f"{volume:.2f}"

print(volume_cone())