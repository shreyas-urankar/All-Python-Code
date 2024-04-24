# Assume you are a teacher of a class, Write a Python program using functions to
# a. Read the names and total marks scored by students of your class of at least 3 or more students
# b. Rank the top 3 students of your class
# c. Provide cash reward of Rs. 5000/- who secured first rank, Rs. 3000/- to the student who
# secured second rank and Rs. 1000/- to the student who secured the third rank. The value of Cash
# reward cannot be modified.

def read_student_info():
    number_of_students = int(input("Enter the number of students:-"))
    student_info = []
    if (number_of_students<3):
        print("Enter minimum 3 students data.")
        number_of_students = int(input("Enter the number of students:-"))

    stdent_info = []
    for i in range (number_of_students):
        name = input(f"Enter the name of student {i+1}: ")
        marks = float(input(f"Enter the total marks by {name}: "))
        student_info.append((name, marks))
    
    return student_info


student_info = read_student_info()
print("\nName \t\tMarks ")
for name, marks in student_info:
    print(f"{name.ljust(15)} {marks}")
























# def read_student_data():
#     num_student = int(input("How many students are there? "))
#     while num_student < 3:
#         print("Minimum 3 students are required.")
#         num_student = int(input("Enter the number of students: "))
    
#     student_data = []
#     for i in range(num_student):
#         name = input(f"Enter the name of student {i+1}: ")
#         marks = float(input(f"Enter the total marks by {name}: "))
#         student_data.append((name, marks))
    
#     return student_data

# student_data = read_student_data()

# print("\nName \t Marks ")
# for name, marks in student_data:
#     print(name, "\t", marks)