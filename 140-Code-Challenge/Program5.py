#Write a Python Program to Find the Sum of Natural Numbers.
limit=int(input("Enter the limit: "))
sum=0
for i in range(1, limit+1):
    sum +=i
print(f"The sum of natural number up to {limit} is {sum}.")