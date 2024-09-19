# Write a Python Program for array rotation.


def rotate_array(arr, d):
    n = len(arr)
    d = d % n

    if d < 0 or n == 0:
        return "Invalid rotation value."
    
    rotated_arr = [0] * n

    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]
        
    return rotated_arr

array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
d = int(input("Enter the number of positions to rotate the array: "))

result = rotate_array(array, d)
print(f"Original Array: {array}.")
print(f"Rotated Array: {result}.")
