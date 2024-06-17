# Write a python function to print first N lines of the following pattern.
# ***
# **
# *  for n=3

n=int(input("Enter the number of * to be printed:"))

def star(n):
    if n==0:
        return n
    print("*" *n)
    star(n-1)

s=star(n)
print(f"The first N lines of pattern is:{s} ")