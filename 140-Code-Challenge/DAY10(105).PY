def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": addition, "-": subtraction, "*": multiplication, "/": divide}

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
calculation_symbol = operations[operation_symbol]
answer = calculation_symbol(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
