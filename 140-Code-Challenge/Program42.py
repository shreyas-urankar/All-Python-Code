# Write a Python program to find second minimum number in a list using sort() function.

numbers = [30, 10, 45, 5, 20]
numbers.sort()
min_val=numbers[0]
print(f"Minimum value in the list is: {min_val}.")

smin_val=numbers[1]
print(f"Second minimum value in the list is: {smin_val}")