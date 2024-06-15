num=input("Enter a number:-")
print("The multiplication table of {num} is as below :-")
try:
    for i in range(1,13):
        print(f"{int(num)} x {int(i)} ={int(num)*i}")
except Exception as e:
    print("Invalid input (Its not an integer).\nPlease enter a valid input (integer). ")
