# Write a Python Program to Check Leap Year
year=int(input("Enter a year:"))
if(year%400==0) and (year%100==0):
    print(f"{year} is a leap year".format(year))
elif(year%4==0)and (year%100!=0):
    print(f"{year} is a leap year".format(year))
else:
    print(f"{year} is not a leap year".format(year))