# Create a classpets from a class animal and further create a class dog from pets and add method bark to class dog.
class Animals:
    pass
class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

d=Dog()
d.bark()
