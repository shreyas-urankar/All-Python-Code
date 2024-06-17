# Write a class calculator capable of finding square, cube, square root of a number.

class Calculator:
    def __init__(self, n) -> None:
        self.n = n

    def square(self):
        return self.n ** 2

    def cube(self):
        return self.n ** 3

    def square_root(self):
        return self.n ** 0.5

# Example usage:
print("-------------Welcome to Calculator.------------------")
n = int(input("Enter a value (n): "))
c = Calculator(n)

print(f"The square of {n} is: {c.square()}")
print(f"The cube of {n} is: {c.cube()}")
print(f"The square root of {n} is: {round(c.square_root(), 2)}")
