# Write a Python program to find second minimum number in a list using remove() function.

numbers = [30, 10, 45, 5, 20]
minval=min(numbers)
print(f"Minimum value in the list is:{minval}")
numbers.remove(minval)
smin=min(numbers)
print(f"Second minimum number in list is:{smin}.")