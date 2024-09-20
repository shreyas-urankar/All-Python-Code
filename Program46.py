#  Write a Python program to find largest number in a list.
numbers = [30, 10, -45, 5, 20]
largest_number=numbers[0]
for i in numbers:
    if i > largest_number:
        largest_number=i
print(f"The largest number in the list is: {largest_number}")