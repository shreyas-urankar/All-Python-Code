#  Write a Python program to Remove empty List from List.
list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
filtered_list=[i for i in list_of_lists if i]
print(f"List after removing empty lists: {filtered_list}")