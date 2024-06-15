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
    
p1 = PersonInformation("Aarav Patel", "23 Gandhi Nagar", "9876543210", "aaravpatel@example.com", "01/01/1990")
p2 = PersonInformation("Diya Sharma", "45 Nehru Road", "9876543211", "diyasharma@example.com", "02/02/1991")
p3 = PersonInformation("Rohan Deshmukh", "67 Rajaji Lane", "9876543212", "rohandeshmukh@example.com", "03/03/1992")
p4 = PersonInformation("Ishaan Gupta", "89 Bose Street", "9876543213", "ishaangupta@example.com", "04/04/1993")
p5 = PersonInformation("Ananya Singh", "101 Tagore Avenue", "9876543214", "ananyasingh@example.com", "05/05/1994")

print(p1.info(),"\n")
print(p2.info(),"\n")
print(p3.info(),"\n")
print(p4.info(),"\n")
print(p5.info(),'\n')