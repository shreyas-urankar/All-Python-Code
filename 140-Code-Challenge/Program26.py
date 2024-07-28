#Write a Python program that simulates a pizza order system, where the user can select the size of the pizza, choose to add pepperoni, and opt for extra cheese, with the program calculating and displaying the final bill


print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L?:-")
bill = 0
print(size)  # What size pizza do you want? S, M, or L

if size == "S":
    bill = 15
    print("Small size pizza is $15.")
elif size == "M":
    bill = 20
    print("Medium size pizza is $20.")
else:
    bill = 25
    print("Large size pizza is $25.")
    want_pepperoni = input("Do you want to add pepperoni? Yes or No")
    if want_pepperoni == "Yes":
        add_pepperoni = input("Add pepperoni for small size pizza. Yes or No")
        if add_pepperoni == "Yes":
            bill += 2
            print("The additional pepperoni on small size pizza will cost $2 on the current bill.")

        add_pepperoni = input("Add pepperoni for medium or large size pizza. Yes or No")
        if add_pepperoni == "Yes":
            bill += 3
            print("The additional pepperoni on medium or large size pizza will cost $3 on the current bill.")

extra_cheese = input("Do you want extra cheese? Yes or No")
if extra_cheese == "Yes":
    bill += 1
    print("Adding extra cheese for any size pizza costs $1.")

print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")


