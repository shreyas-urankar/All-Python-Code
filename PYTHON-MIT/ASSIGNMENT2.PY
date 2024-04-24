# write a program to use input built in function , to take  a string input from the user , what they just typed in
# add another piece of similar code but have the input be numeric  , also write a code to detect whether a number 
# positive negative or 0 , try using a fixed value at first then update your program to accept numeric input
# from the user IN PYTHON

s=str(input("Enter a string:-"))
print("typed in",s)
num=float(input("Enter a number:-"))
if(num<0):
    print("Number is a negative number.")
elif(num>0):
    print("Number is a positive number.")
else:
    print("Number is equal to 0.")