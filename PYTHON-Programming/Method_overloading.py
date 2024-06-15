class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print("Area of Rectangle",(a*b))
        elif a!=None:
            print("Area of Rectangle",(a*a))
        else:
            print("Nothing to find")
obj=Area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)