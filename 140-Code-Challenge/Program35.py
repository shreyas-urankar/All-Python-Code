# Write a Python Program to Sort Words in Alphabetic Order.
my_str=input("Enter a strig:")
words =[word.capitalize() for word in my_str.split()]

words.sort()
print("The shorted words are:")
for word in words:
    print(word)