# class_student=[('Kedar', 18, 'Sy-Core'), ('chandan', 13, 'Sy-core'), ('krishna', 19, 'Sy-core'), ('gaurav', 16, 'Sy-core'), ('sameer', 29, 'Sy-core'), ('arpit', 5, 'sy-core'), ('anushka', 7, 'sy-Core'), ('divya', 12, 'sy-core'), ('sonukumar', 42, 'sy-core'), ('shreyas', 38, 'sy-core')]
# # x=input("Enter name to serach student information:- ")
# # for student in class_student:
# #        if(x==student[0]):
# #            print(student)
    
# for i in range(0,2):
#         a=input("Enter name of student:- ")
#         b=int(input("Enter Roll No:- "))
#         c=input("Enter Division:- ")
#         class_student.append([a,b,c]) 
        
# print("\n")
# print("-------------------------------------------------------------------------------------------")
# print("\n")
# class_student.pop()
# print(class_student)




# on amazon website we have the following available items amazon_website=[("watch",100), ("phone",200),("laptop",300),("shirt",400)].
# take the user input N no of times and find out the total cost to be paid. If the item is not present in the amazon website 
# then print that item as out of stock and do add it total. use for loop in python.


amazon_website = [("watch", 100), ("phone", 200), ("laptop", 300), ("shirt", 400)]

N = int(input("Enter the number of items you want to purchase: "))
total_cost = 0
out_of_stock_items = []
chosen_items = {}

for i in range(N):
    choice = input(f"Enter item {i + 1} name: ").lower()
    if choice not in chosen_items:
        chosen_items[choice] = 1
    else:
        chosen_items[choice] += 1

    # found = False
for item_name,quantity in chosen_items.items():
    found=False
    for product, price in amazon_website:
        if item_name == product:
            total_cost += price * quantity
            found = True
            break
    if not found:
        out_of_stock_items.append(item_name)

print(f"Total cost to be paid:Rs {total_cost}")

if out_of_stock_items:
    print("Out of stock items:")
    for item in out_of_stock_items:
        print(item)
