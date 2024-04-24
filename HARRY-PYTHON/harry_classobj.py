class Person:
    def __init__ (self,name,occupation):
        print("Hey im a person.")
        self.name=name
        self.occupation=occupation
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person("Shreyas", "HR")
b=Person("Madhura","Business women")
a.info()
b.info()