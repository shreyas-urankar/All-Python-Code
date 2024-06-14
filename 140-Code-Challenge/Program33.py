# Write a Python Program to Split the array and add the first part to the end

def split_and_add(arr, k):
    if k<=0 or k>=len (arr):
        print("Element does not exist in the given array")
        return None


    first_part =arr[:k]
    second_part=arr[k:]

    result = second_part + first_part
    return result


arr=[1,2,3,4,5]
k=6
result=split_and_add(arr, k)

if result is not None:
    print(f"Original Array is: {arr}")
    print(f"Array after splitting and adding is: {result}.")


