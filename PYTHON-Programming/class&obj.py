# # class Student:
# #     name="Shreyas"

# # s1=Student()
# # print(s1.name)

# class Student:
#     college_name="MIT ADTU"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome student," , self.name)

#     def get_marks(self):
#         return (s1.marks)
# s1 = Student("Shreyas",99)
# print(s1.name, s1.marks)
# s1.welcome()
# print(s1.get_marks())

# s2 = Student("Madhura", 98)
# print(s2.name, s2.marks)
# s2.welcome()
# print(s2.college_name)
# print(Student.college_name)

# Practice Que

# Create student class that takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to print the average

class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum +=val
        print("hi", self.name, "your avg score is:-",sum/3)
    
s1=Students("Shreyas",[99,98,97])
s1.get_avg()
s1=Students("Madhura",[1,2,3])
s1.get_avg()

