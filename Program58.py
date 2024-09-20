# Write a Python Program to check if a string contains any special character.

def check_special_char(in_str):
    return any(char in "!@#$%^&*()_+{}[]:;<>,.?~\\/\'\"-=" for char in in_str )
input_string = input("Enter a string:")
if check_special_char(input_string):
    print("The string contains special characters:")
else:
    print("The string does not contains special characters.")