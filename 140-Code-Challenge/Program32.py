# Write a Python Program to find largest element in an array.
def find_largest_element(array):
    if not array:
        return "Array is empty."
    

    largest_element=array[0]

    for element in array:
        if element> largest_element:
            largest_element=element
    return largest_element

array=[10,56,92,100,169,83]
result=find_largest_element(array)
print(f"The largest element in the aray in the array is: {result}.")