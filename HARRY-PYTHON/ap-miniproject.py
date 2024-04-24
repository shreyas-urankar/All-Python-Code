first=input("Enter the first number:-")
operator=input("enter operator(+,-,*,/,%):-")
second=input("Enter the second number:-")

first=int(first)
second=int(second)
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first // second)
elif operator == "%":
    print(first % second)
else:
    print("Enter the the correct operator")