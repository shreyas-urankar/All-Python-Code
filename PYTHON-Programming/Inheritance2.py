class Employee:
    company = "ITC"  # Class attribute

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}. The company is {Employee.company}.")

class Programmer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def showLanguage(self):
        print(f"The name is {self.name} and he is a good programmer with {self.language} language.")

# Create an instance of Programmer
a = Programmer("Shreyas", 7000000, "Python")
a.show()
a.showLanguage()
