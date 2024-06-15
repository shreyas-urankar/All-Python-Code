class B1:
    def __init__(self):
        print("B1 init")
    def __del__(self):
        print("B1 del")

class B2:
    def __init__(self):
        print("B2 init")
    def __del__(self):
        print("B2 del")
class D(B1,B2):
    def __init__(self):
        B2.__init__(self)
        print("D init")
    def __del__(self):
        B1.__del__(self)
        B2.__del__(self)
        print("D del")
d=D()
d=None
