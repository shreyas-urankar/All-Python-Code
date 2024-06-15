# Write a python code that prompts user to input a number (n). Then your code will list all the
# numbers (1-n) with a comma after each number except for the last number. There should be 10
# numbers per line.
# a. Using for loop Structure
# b. Using while loop structure

# num = int(input("Enter a number:-"))
# print(num)

# for i in range(1, num + 1):

#     print(i, end=" ")
#     if i == num:
#         print()
#     else:
#         print(",", end=" ")

        # while loo
num = int(input("Enter a number: "))
print(num)

i = 1
while i <= num:
    print(i, end=" ")
    if i == num:
        print()
    else:
        print(",", end=" ")
    i += 1
