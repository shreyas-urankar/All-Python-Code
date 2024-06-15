# def showdata():
#     print("Welcome to the Shreyas Python Programming.")
# showdata()


# Functions arguments

# def sum(a,b):
#     print(a+b)
# sum(1,2)


# def square(x=5):
#     return x*x
# s=square(10)
# print(s)

# .....................................................

# def cal_avg(a,b,c,):
#     sum = a + b + c
#     avg = sum // 3
#     print(avg)
# cal_avg(1,2,3)


# PRACTICE QUESTIONS
# Q1) WAF TO PRINT THE LENGTH OF A LIST. (LIST IS THE PARAMETER)

# num = ["1","2","3","4","5"]
# cities =["Pune","Pimpri","Mumbai","Banglore","Chennai","Bhopal"]

# def print_len(list):
#     print(len(list))
# print_len(num)
# print(len(cities))
# print(cities[5])

# ........................................................
# Q2) WAF TO PRINT THE ELEMENT OF A list in a single line.(list is the parameter)
# num = ["1","2","3","4","5"]
# cities =["Pune","Pimpri","Mumbai","Banglore","Chennai","Bhopal"]

# def print_len(list):
#     print(len(list))
# print_len(num)
# print_len(cities)

# def print_straight(list):
#     for i in list:
#         print(i, end=" ")
# print_straight(num)
# print()
# print_straight(cities)
#..........................................................
# Q3) WAF TO FIND THE FACTORIAL OF N.(N IS THE PARAMETER)

# def cal_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *=i
#     print(fact)
# cal_fact(5)
# ..........................................................
# Q4) WAF TO CONVERT USD TO INR
def con_usd(dollers):
    INR = 83
    for i in range(1,dollers+1):
        INR *= i
    print(f"{dollers} Dollers id equal to RS {INR}")

dollers = int(input("Enter the amount in dollers:-"))
con_usd(2)