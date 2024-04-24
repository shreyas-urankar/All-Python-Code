height=int(input("What is your height in feet?"))
print(height)
if height>=3:
    print("You can ride")
    age=int(input("What is your age?"))
    print(age)
    if age<=18:
        print("Pay Rs 5000 ")
    else:
        print("You dont need to pay any")
else:
    print("You cant ride")
print("Bye have a nice day")