# Write a Python program to print odd numbers in a list.
elements = input("Enter the elements of the list separated by spaces: ")
numbers = [int(x) for x in elements.split()]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Even numbers in the list:", odd_numbers)
