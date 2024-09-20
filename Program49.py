# Write a Python program to print even numbers in a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers=[num for num in numbers if num%2==0]
print(f"Even numbers in hte list: {even_numbers}")