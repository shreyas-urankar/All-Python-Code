# Write a Python program to Extract Unique dictionary values.


my_dict = {
 'a': 10,
 'b': 20,
 'c': 10,
 'd': 30,
 'e': 20
 }

unique_values=set()

for i in my_dict.values():
    unique_values.add(i)

unique_values_list=list(unique_values)
print(f"Unique values in the dictionary: {unique_values_list}")

