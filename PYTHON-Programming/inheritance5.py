# Create a class employee and add salary and increment properties to it.

class Employee:
    def __init__(self, salary=234, increment=20):
        self.salary=salary
        self.increment=increment
e=Employee()
print(f"Salary: {e.salary}")
print(f"Increment: {e.increment}")

e.salary=500
e.increment=50

print(f"Updated Salary: {e.salary}")
print(f"Updated Increment: {e.increment}")