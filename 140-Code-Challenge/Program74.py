# Create a function that takes a list of strings and integers, and filters out the list so
# that it returns a list of integers only.

def filter_list(lst):
    return [x for x in lst if isinstance(x, int)]
input_str = input("Enter elements (strings and integers) separated by spaces: ")
elements=input_str.split()
processed_elements=[]
for ele in elements:
    try:
        processed_elements.append(int(ele))
    except ValueError:
        processed_elements.append(ele)

result=filter_list(processed_elements)
print(f"Filtered list of integers: {result}")