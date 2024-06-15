# Write a Python program to find all duplicate characters in string.
def find_duplicates(input_string):
    char_count = {}
    duplicates = []

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)

    return duplicates

input_string = "shreyas urankar"
duplicate_chars = find_duplicates(input_string)
print("Duplicate characters:", duplicate_chars)
