# Write a Python Program to Remove Punctuation From a String.
punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str=input("Enter a string with didicated punctuations:")
no_punct=""
for char in my_str:
    if char not in punctuation:
        no_punct=no_punct + char

print(f"Your string after removing dedicated punctions is: \n{no_punct}")