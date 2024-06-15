# WRITE A PROGRAM USING FOR LOOP TO CALCULATE THE AVERAGE OF FIRST N NATURAL NUMBERS

n = int(input("Enter the vale of n:-"))
avg=0.0
sum=0
for i in range(1,n+1):
    sum=sum+i
avg=sum//i
print(f"The sum of first {n} natural number is:- {sum}")
print(f"The average of first {n} natural number is:- {avg}")