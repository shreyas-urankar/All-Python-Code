# trunk-ignore-all(black)
#  Write a Python Program to Remove Punctuation From a String.
punctuations=r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str=input("Enter a string:")
no_punctuations=""
for char in my_str:
    if char not in punctuations:
        no_punctuations=no_punctuations+char

print(no_punctuations)