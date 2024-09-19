# Write a Python program to split and join a string.
input_str=input("Enter a string:")
word_list=input_str.split()
separetor= " "
output_str=separetor.join(word_list)
print(f"Original String: {input_str}")
print(f"List of split Words: {word_list}")
print(f"Joined String: {output_str}")
