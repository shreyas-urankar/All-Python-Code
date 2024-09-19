# Write a Python Program for cube sum of first n natural numbers?
def cube_sum_of_natural_numbers(n):
    if n <=0:
        return 0
    else:
        total=sum([i**3 for i in range(1, n+1)])
        return total
    
num=int(input("Enter a number: "))
if num < 0:
    print("Please enter a positive number.")
else:
    result = cube_sum_of_natural_numbers(num)
    print(f"The cube of sum of first {num} natural number is {result}.")