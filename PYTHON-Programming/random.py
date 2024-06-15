# Write a python program to convert the kilometers to miules
# Q1)calculate area of triangle
# Q2)calculate square and cube of given number
# Q3)input the quadratic equation and find the value of x

# Ans1)
# h=input("Enter the height of the triangle:-")
# b=input("Enter the base of the triangle:-")
# area=0.5*(int(b)*int(h))
# print(int(area))

# Ans 3)

import cmath

print("General Form;- ax**2+bx+c=0")
a=int(input("Enter a:-"))
b=int(input("Enter b:-"))
c=int(input("Enter c:-"))

d=(b**2)-(4*a*c)
roots1=(-b+cmath.sqrt(d)/(2*a))
roots2=(-b-cmath.sqrt(d)/(2*a))
print("\n")
print(f"Result for quadratic equation are:-{a}x**2+{b}x+{c}=0, are:-")
print(f"The solutions are {roots1} and {roots2}")
if d>0:
    print("Type of Roots:- Real And Distinct Roots")
elif d==0:
    print("Type of Roots:-Real And Repeated Roots")
elif d<0:
    print("Type of Roots:-Imaginary And Distinct Roots")










