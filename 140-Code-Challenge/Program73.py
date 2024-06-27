# Using list comprehensions, create a function that finds all even numbers from 1 to the given number.
def even_numbers(num):
    return [z for z in range(1, num+1) if z % 2 == 0]

input_str = input("Enter the values of num (separated by spaces): ")
nums = map(int, input_str.split())

for num in nums:
    result = even_numbers(num)
print(f"Even numbers from 1 to {num} are: {result}.")
