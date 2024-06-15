#  Write a program to have the user input three (3) numbers: from, to and increment.Count from f 
# to t in increments of I, inclusive of f and t. 
# For example, if the input is 
# f==2, t==26, and i==4, the program would show output 2,6,10,14,18,22.

start=int(input("Enter the number:-"))
end=int(input("Enter the end number:-"))
increment=int(input("Enter the increment number"))

for i in range(start, end, increment):
    print(i)
               

