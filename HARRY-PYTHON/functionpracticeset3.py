# Writer recursive function to calculate the sum of first n natural numbers

n=int(input("Enter the vale for n:"))

def sum(n):
    if n==1:
        return 1
    return sum(n-1)+n

value=sum(n)
print(f"The sum of first {n} natural number is: {value}. ")