# Write a program to accept Persons information as Name,Address,Phone number ,Email, and Date of birth. Make use of initialiser to set up a new object. Accept the records for at least 5 persons.
class PersonInformation:
    def __init__(self,name,address,phno,email,dob):
        self.name=name
        self.add=address
        self.phno=phno
        self.email=email
        self.dob=dob
    def info(self):
        return(f"Your name is:- {self.name}.\nYour address is:- {self.add}.\nYour Phone Number is:- {self.phno}.\nYour Email id is:- {self.email}.\nYour Date Of Birth is:- {self.dob}.")
    
persons=[]

for i in range(2):
    print(f"Enter the details of Person {i+1}:-")
    name=input("Enter your name:-")
    address = input("Enter Address:- ")
    phno = input("Enter Phone Number:- ")
    email = input("Enter Email:- ")
    dob = input("Enter Date of Birth:- ")
    persons.append(PersonInformation(name,address,phno,email,dob))
    print()

for person in persons:
    print(person.info())
    print(persons[-1].info())
    print("\n")