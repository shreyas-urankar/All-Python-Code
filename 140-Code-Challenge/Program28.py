# Write a Python Program to find sum of array.

def sum_of_array(arr):
    total = 0
    for element in arr:
        total += element
    return total

array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
result = sum_of_array(array)
print("Sum of the array is:", result)
