class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def info(self):
        print(f"Hi, I'm {self.name}, and I'm a {self.role} at the university")

class Student(Person):
    def __init__(self, name, role, student_id):
        super().__init__(name, role)
        self.student_id = student_id
    
    def info(self):
        super().info()
        print(f"My student ID is {self.student_id}.")

class Staff(Person):
    def __init__(self, name, role, staff_id):
        super().__init__(name, role)
        self.staff_id = staff_id
    
    def info(self):
        super().info()
        print(f"My staff ID is {self.staff_id}.")

class Administrative(Person):
    def __init__(self, name, role, admin_id):
        super().__init__(name, role)
        self.admin_id = admin_id
    
    def info(self):
        super().info()
        print(f"My admin ID is {self.admin_id}.")

def get_person_info():
    name = input("Enter name: ")
    role = input("Enter role (student/staff/administrative): ")
    if role.lower() == "student":
        student_id = input("Enter student ID: ")
        return Student(name, role, student_id)
    elif role.lower() == "staff":
        staff_id = input("Enter staff ID: ")
        return Staff(name, role, staff_id)
    elif role.lower() == "administrative":
        admin_id = input("Enter admin ID: ")
        return Administrative(name, role, admin_id)
    else:
        print("Invalid role. Please enter 'student', 'staff', or 'administrative'.")
        return None

if __name__ == "__main__":
    num_people = int(input("Enter the number of people: "))
    people = []
    for i in range(num_people):
        print(f"Enter the details of person {i+1}:")
        person = get_person_info()
        if person:
            people.append(person)

    print("\nDetails of people:")
    for person in people:
        person.info()
