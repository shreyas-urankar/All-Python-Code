# Create a class programmer for storing information of few programmers working at Microsoft.

class Programmers:
    print("Programmers are working at Microsoft.")
    def __init__(self, name,salary, pin ) -> None:
        self.name=name
        self.salary=salary
        self.pin=pin
    

p=Programmers("Shreyas", 120000, 411040)
print(p.name, p.salary, p.pin)