class Shreyas:
    def displayinfo(self):
        print("Welcome to Shreyas's House.")

class Urankar(Shreyas):
    def displayinfo(self):
        super().displayinfo()
        print("Welcome to Urankar's House.")
obj=Urankar()
obj.displayinfo()