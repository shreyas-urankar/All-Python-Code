# Write a Python program to check if the given number is a Disarium Number.
#  A Disarium number is a number that is equal to the sum of its digits each raised to the
#  power of its respective position.

def is_disarium(number):
    num_str=str(number)
    digit_sum=sum(int(i)**(index+1) for index, i in enumerate(num_str))
    return digit_sum==number

try:
    num=int(input("Enter a number:"))
    if is_disarium(num):
        print(f"{num} is a Disarium number.")
    else:
        print(f"{num} is not a Disarium number.")
except ValueError:
    print("Invalid output. Please enter a valid number.")