# WRITE A PROGRAM TO PRINT THE MULTIPLICATION TABLE OF N, WHERE N IS ENTERED BY THE USER.

n = int(input("Enter the number:-"))
print(f"Multiplication table of {n} is:-")
print("***********************************")
for i in range(1,13):
    print(n, "X", i, "=", n*i)