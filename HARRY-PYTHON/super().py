class Employee:
    def __init__(self,name, id):
        self.name=name
        self.id=id

class Programmer(Employee):
    def __init__(self,name, id,lang):
        super().__init__(name, id)
        self.lang=lang

shreyas=Employee("Shreyas","2004")
print(shreyas.name)
print(shreyas.id)
sonu=Programmer("Sonu","2003","WT")
print(sonu.name)
print(sonu.id)
print(sonu.lang)