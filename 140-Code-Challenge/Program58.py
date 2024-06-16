# Please write a program using generator to print the even numbers between 0 and n in
# comma separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10

def Even_Numbers(n):
    for i in range(n+1):
        if i%2==0:
            yield i

try:
    n=int(input("Enter a value for n:"))
    result=Even_Numbers(n)
    print(','.join(map(str, result)))

except ValueError:
    print("Invalid input. Please enter a valid integer for n.")