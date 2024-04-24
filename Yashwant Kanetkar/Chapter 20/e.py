from abc import ABC,abstractmethod
class Vehical():
    @abstractmethod
    def speed(self):
        pass
    def maintenance(self):
        pass
    def value(self):
        pass
class FourWheeler(Vehical):
    def speed(self):
        print("This is FourWheeler speed.")
    def maintenance(self):
        print("Maintenance of FourWheeler.")
    def value(self):
        print("Value of FourWheeler.")
class TwoWheeler(Vehical):
     def speed(self):
        print("This is TwoWheeler speed.")
     def maintenance(self):
        print("Maintenance of TwoWheeler.")
     def value(self):
        print("Value of TwoWheeler.")
fw=FourWheeler()
fw.speed()
fw.maintenance()
fw.value()
tw=TwoWheeler()
tw.speed()
tw.maintenance()
tw.value()


    