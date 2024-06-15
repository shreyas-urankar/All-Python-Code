from abc import ABC,abstractmethod
class Printer(ABC):
    def __init__(self,n):
        self.n=n
    @abstractmethod
    def print(self, docName):
        pass

class LaserPrinter(Printer):
    def __init__(self,n):
        super().__init__(n)

    def print(self,docName):
        print("LeaserPrinter")
        print("Trying to print:-",docName)

class Inkjetprinter(Printer):
    def __init__(self,n):
        super().__init__(n)

    def print(self,docName):
        print("Inkjetprinter")
        print("Trying to print:-",docName)

l=LaserPrinter("LaserJet")
l.print("hello1.pdf")
l=Inkjetprinter("Inkjetprinter")
l.print("hello2.pdf")
