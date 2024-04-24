def greet(name, subject ,dept):
    print(f"Hi {name} and do you teach {subject}.")
    print(f"Are you from {dept} department?")
greet("Shreyas","Maths","IT")


def add(*numbers):
    c=0
    for i in numbers:
     c=c+i
    print(f"Sum is {c}.")
add(5,7,6,5,2)