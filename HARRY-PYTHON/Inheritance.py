class A:
    def displayA(self):
        print("Welcome to Python A")

class B(A):
    def displayB(self):
        print("Welcome to Python B")

obj=B()
obj.displayA()
obj.displayB()