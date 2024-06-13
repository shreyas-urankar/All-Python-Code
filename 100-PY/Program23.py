# Write a Python Program to Find HCF.
# Highest Common Factor(HCF)

num1=int(input("Enter the first number:\n"))
num2=int(input("Enter the second number:\n"))

def compute_hcf(x, y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1, smaller+1):
        if(x%i==0)and(y%i==0):
            hcf=i
    return hcf
print(f"The HCF of there two numbers is {compute_hcf(num1, num2)}.")