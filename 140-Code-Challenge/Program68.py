# Write a function that calculates the factorial of a number recursively.

def factorial_recursively(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial_recursively(n-1)
    
n=int(input("Enter the value for n:"))
result=factorial_recursively(n)
print(f"The factorial value of {n} is:{result}.")