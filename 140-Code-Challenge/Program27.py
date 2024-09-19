#Write a Python program that simulates a rollercoaster ticketing system, where the user inputs their height and age to determine eligibility and ticket price, and optionally adds a photograph to the final bill.


print("Welcome to the rollercoaster!")
bill=0
height = int(input("Enter your height:- "))
print(height)

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age:- "))
    print(age)

    if age < 12:
        bill=50
        print("Children tickets are Rs 50 per person.")
    elif age <= 18:
        bill=150
        print("Youth tickets are Rs 150.")
    else:
        bill=250
        print("Adults tickets are Rs 250.")

        want_photograph=input("Do you wan ta photo taken? Yes or No:-")
        if want_photograph=="Yes":
            print("The photography cost additional Rs 30 on current bill")
            bill+=30
            print(f"Your final bill is {bill}.")
else:
    print(
        "Sorry, your height does not meet our requirement of a minimum height of 120.")
    
