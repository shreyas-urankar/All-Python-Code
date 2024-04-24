# Write a program to perform the following on Tuple
# a. Write a program to create a tuple of 4 elements.
# b. Convert this tuple into a list.
# c. Now delete the first element in this list and convert it back to tuple.

# Code a:-
new_tuple = (1, 2, 3, 4)
print("Original tuple:", new_tuple)

# Code b:-
new_list = list(new_tuple)
print("Original list:", new_list)

# Code c:-
del new_list[0]
modified_tuple = tuple(new_list)
print("Modified tuple:", modified_tuple)

