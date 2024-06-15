class DemoClass:
    a=10

    def sumvalue(self):
        print(20+30)
demoobj=DemoClass()
print(demoobj.a)
demoobj.sumvalue()

class Employee:

    def set_data(self,n,a,s):
        self.name=n
        self.age=a
        self.salary=s
    def display_data(self):
        print(f"Hi employee name is {self.name} and his/her age is {self.age} and salarys is Rs {self.salary}")
e=Employee()
e.set_data("Shreyas",20,100000000)
e.display_data()
e.set_data("Ram",21,200000)
e.display_data()

class Number:
    def __init__(self):
        self.self_num = None  
    
    def set_number(self, n):
        self.self_num = n
    
    def get_number(self):
        return self.self_num
    
    def print_number(self):
        print(self.self_num)
    
    def isnegative(self):
        if self.self_num < 0:
            return True
        else:
            return False
        
    def isdivisible(self, divisor):
        if divisor == 0:
            return False
        if self.self_num % divisor == 0:
            return True
        else:
            return False
        
    def absolute_values(self):
        if self.self_num > 0:
            return self.self_num
        else:
            return -1 * self.self_num

x = Number()
x.set_number(2)
x.print_number()
print(x.isnegative())
print(x.isdivisible(2))  

class Fruit:
    count=0
    def __init__(self,name,color,size):
        self.name=name
        self.color=color
        self.size=size
        Fruit.count+=1
    def display(self):
        print(f"Name of the fruit is {self.name} and size is {self.size} and color is {self.color}.")
        print(f"Total number of fruits:- {Fruit.count} Fruits")
apple=Fruit("Apple","Red",10)
apple.display()
orange=Fruit("Orange","orange",5)
orange.display()

