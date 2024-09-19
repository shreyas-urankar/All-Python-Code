# Write a Python Program to Display the multiplication Table.
num=int(input("Enter a number:"))
print(f"The multiplication of {num} from 1 to 10 is: ")
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")