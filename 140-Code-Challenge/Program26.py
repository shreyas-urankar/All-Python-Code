print("Mini Calculator")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
print("Press 1 for addition.\nPress 2 for subtraction.\nPress 3 for multiplication.\nPress 4 for division.")
choice = int(input("Enter you choice from (1-4):"))
if choice ==1:
    print(f"Addition of {num1} and {num2} is {num1 + num2}.")
elif choice==2:
    print(f"Subtraction of {num1} and {num2} is {num1 - num2}.")
elif choice ==3:
    print(f"Multiplication of {num1} and {num2} is {num1 * num2}.")
elif choice==4:
    print(f"Division of {num1} and {num2} is {num1 / num2}.")
else:
    print("You have entered wrong option. Please enter option between 1-4.")