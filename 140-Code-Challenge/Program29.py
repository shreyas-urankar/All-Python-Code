# Write a Python Program to find largest element in an array.

def largest_element(arr):
    if not arr:
        return "Array is empty."
    largest_element =arr[0]
    for element in arr:
        if element > largest_element:
            largest_element=element 
    return largest_element
array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
result = largest_element(array)
print(f"The largest element in the array is: {result}.")
