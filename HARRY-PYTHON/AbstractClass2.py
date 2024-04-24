from abc import ABC,abstractmethod
class Character(ABC):
    @abstractmethod
    def patriotism(self):
        pass

class Actor(Character):
    def style(self):
        pass

class Person(Actor,Character):
    def do_acting(self):
        print("Person doing acting.")
    def style(self):
        print("Person Acting style.")
    def patriotism(self):
        print("Great")

p=Person()
p.patriotism()
p.style()
p.do_acting()
