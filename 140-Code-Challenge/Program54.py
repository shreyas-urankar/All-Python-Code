# Write a program that accepts a sentence and calculate the number of letters and
# digits. Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

string=input("Enter a sting:")

def countLetterAndDigit(string):
    lcount=dcount=0
    for c in string:
        if c.isdigit():
            dcount +=1
        elif c.isalpha():
            lcount +=1
    return lcount, dcount

letter, digits= countLetterAndDigit(string)
print(f"Number of letters:{letter}")
print(f"Number of alphabets:{digits}")