#Write a Python Program to check if given array is Monotonic.
 #A monotonic array is one that is entirely non-increasing or non-decreasing

def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False
    
    return increasing or decreasing 

array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
result = is_monotonic(array)
print(f"The array is monotonic: {result}.")
