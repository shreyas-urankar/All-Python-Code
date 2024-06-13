# Write a Python Program to Find Factorial of Number Using Recursion.

def recursion_factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*recursion_factorial(n-1)
num=int(input("Enter the number:"))
if num<0:
    print("Sorry, factorial does not exist for negative integer.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    print(f"The factorial of {num} is {recursion_factorial(num)}.") 
