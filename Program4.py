#Write a Python program to solve quadratic equation.
# The standard form of a quadratic equation is:𝑎x^2 +𝑏𝑥+𝑐=0, where
 #a, b and c are real numbers and 𝑎 ≠ 0
 #The solutions of this quadratic equation is given by:
# (−𝑏 ± (b^2 −4𝑎𝑐 )^1/2/(2𝑎))

import math
a=float(input("Enter coefficient a: "))
b=float(input("Enter coefficient b: "))
c=float(input("Enter coefficient c: "))

discriminant = b**2 -4*a*c
if discriminant >0:
    root1=(-b + math.sqrt(discriminant)) / (2*a)
    root2=(-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif discriminant == 0:
    root = -b /(2*a)
    print(f"Root: {root}")
else:
    real_part =-b/(2*a)
    imaginary_part =math.sqrt(abs(discriminant)) /(2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")