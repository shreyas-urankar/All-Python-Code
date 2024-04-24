# Write a program to perform the following on List
# a. Enter a List of Numbers and sort the value in Largest-to-smallest order.
# b. Do the same thing, but for strings and in reverse alphabetical order.
# c. Create a list with elements as "apple", "banana","cherry","kiwi","mellon","mango".
#    Display each with its position
# d. Insert "Orange",then Copy list into another list.
# e. Remove "cherry" from first list and dislay both the srings.
# f. Display the third, fourth, and fifth item of first list.
# g. Check if "apple" is present in the list display message as present.
# h. And then print all items in the list, one by one
# i. To delete element at third index and perform pop().


# Answer (a)

# list1=["9","8","4","10","2","5","1","3","6"]
# list1= [int(x) for x in list1]
# list.sort()
# print(list1)
# len(list1)
# print(len(list1))


# Answer(b)

# list1 = ["a", "z", "c", "k", "v"]
# list1.sort(reverse=True)
# print(list1)


# Answer (c)

# list3 = ["apple", "banana", "cherry", "kiwi", "mellon", "mango"]
# print(list3[0])
# print(list3[1])
# print(list3[2])
# print(list3[3])
# print(list3[4])
# print(list3[5])
# for i, list3 in enumerate(list3,start=1):
#     print(f"At position {i}:{list3}")

# Answer (d)

# list4 = ["apple", "banana", "cherry", "kiwi", "mellon", "mango"]
# print(list4)
# list4.append("orange")
# print(list4)

# Answer (e)

# list5 = ["apple", "banana", "cherry", "kiwi", "mellon", "mango"]
# print(list5)
# list5.remove("cherry")
# print(list5)

# Answer (f)

# list6 = ["apple", "banana", "cherry", "kiwi", "mellon", "mango"]
# print(list6[3])
# print(list6[4])
# print(list6[5])

# Answer (g)

# list7 = ["apple", "banana", "cherry", "kiwi", "mellon", "mango"]
# if "apple" in list7:
#     print ("apple is present in the list.")
# else:
#     print("appleis not present in the list.")


# Answer (h)

# list8 = ["apple", "banana", "cherry", "kiwi", "mellon", "mango"]
# for fruits in list8:
#     print(fruits)


# Answer (i)

# list9 = ["apple", "banana", "cherry", "kiwi", "mellon", "mango"]
# print(list9)
# list9.pop(3)
# print(list9)

list10 = ["apple", "banana", "cherry", "kiwi", "mellon", "mango"]
list11=[5,6,8,9]
print(max(list10))
print(max(list11))

print(min(list10))
print(min(list11))
