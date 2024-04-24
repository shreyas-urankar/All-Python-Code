# While loop to count number form 1 to 5
# count=1
# while count<=5:
#     print(count)
#     count +=1
# print("Loop Ended")

# while loop to count numbers reverse from 5 to 1
# count =5
# while count>=1:
#     print(count)
#     count -=1
# print("Loop ended")

# Print numbers from 1 to 100 using while loop

# count=1
# while count<=100:
#     print(count)
#     count += 1
# print("Loop Ended")

# Print numbers from 100 to 1 using while loop

# count = 100
# while count>=1:
#     print(count)
#     count -=1
# print("Loop Ended")

# Print a multiplication table of a number n using while loop

# n=int(input("Enter a number:-"))
# count=1
# while count<=10:
    # print(f"{n} X {count} = {n*count}")
    # count +=1

# Print the elements of the following list using a loop
# [1,4,6,16,25,36,49,64,81,100]

# num=[1,4,6,16,25,36,49,64,81,100]
# index=0
# while index<len(num):
#     print(num[index])
#     index +=1

# fruits=["apple","mango","grapes","banana"]
# index =0
# while index<len(fruits):
#     print(fruits[index])
#     index += 1

# Search for a number x in this tuple using while loop
# (1,4,6,16,25,36,49,64,81,100)

num=(1,4,6,16,25,36,49,64,81,100)
x=int(input("Enter a number to search:-"))
# found=False
i=0
while i<len(num):
    if (num[i] == x):
        print(f"Found {x} at index:-{i}")
        # found=True
        break
    else:
        print("Finding...")
    i +=1
print("Loop ended ")

