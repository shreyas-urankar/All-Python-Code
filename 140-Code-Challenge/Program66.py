# Create a function that returns True if a given inequality expression is correct and
# False otherwise.
# Examples
# correct_signs("3 < 7 < 11") ➞ True
# correct_signs("13 > 44 > 33 <1") ➞ False
# correct_signs("1 < 2 < 6 < 9 > 3") ➞ True


class InequlityChecker:
    def check_expression(self,expression):
        try:
            return eval(expression)
        except ValueError:
            print(f"Error evaluating expression: {ValueError}")
            return False
        
check=InequlityChecker()
expression=input("Enter an inequality expression: ")
result=check.check_expression(expression)
print(f"Result:{result}")