# WRITE A PROGRAM TO CHECK IF A NUMBER IS DIVISIBLE BY BOTH 10 AS WELL AS 50. IF IT DIVISIBLE 30 
# AS WELL AS PRINT "THIS NUMBER IS DIVISIBLE BY 10,50 AND 30". IF NOT PRINT THIS NUMBER IS DIVISIBLE BY 
# 10 AND 50 BUT NOT 30. WRITE A PROGRAM.

a=int(input("Enter a number:-"))
if(a%10 and a%50):
    print("The number is divisible by both 10 and 50.")
elif(a%30):
    print("The number is divisible by 10,50 and 30.")
else:
    print("This number is divisible by 1o and 50 but not 30.")