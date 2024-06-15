# Write a Python program to Count occurrences of an element in a list.
my_l=[10,20,30,40,50,10,20,55,36,78,10,52,10,10]
x=10
count=0

for element in my_l:
    if element  == x:
        count +=1
print(f"The count of element occurence in a list is: {count}")
