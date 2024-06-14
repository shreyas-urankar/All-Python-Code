# Write a Python Program for cube sum of first n natural numbers
def cube_of_sum_of_first_n(n):
    sum=0
    for i in range(1, n+1):
        sum +=i**3
    return sum
n=int(input("Enter a number:"))
print(f"The cube sum of first {n} natural numbers is: {cube_of_sum_of_first_n(n)}.")