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
    
p1 = PersonInformation("Shreyas Urankar", "Wanawadi", "9822936024/8010055172/9960774689", "shreyas9898@gmail.com", "12/04/2004")
p2 = PersonInformation("Sameer Dhavale", "Hadapsar", 9090909090, "ss123@gmail.com", "21/03/2004")
p3 = PersonInformation("Sonu Kumar", "Patas", 7897900910, "Sonu555@gmail.com", "21/05/2004")
p4 = PersonInformation("Krishkant Laxne", "Nagpur", 5678909786, "krishna90@gmail.com", "28/03/2003")
p5=PersonInformation("Kedar Kulkarni", "Loni Kalbhor", 8979000010, "kk123@gmail.com", "26/12/2004")
print(p1.info(),"\n")
print(p2.info(),"\n")
print(p3.info(),"\n")
print(p4.info(),"\n")
print(p5.info(),'\n')