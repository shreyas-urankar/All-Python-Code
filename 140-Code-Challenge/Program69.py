# You can assign variables from lists like this:
# lst = [1, 2, 3, 4, 5, 6]
# first = lst[0]
# middle = lst[1:-1]
# last = lst[-1]
# print(first) ➞ outputs 1
# print(middle) ➞ outputs [2, 3, 4, 5]
# print(last) ➞ outputs 6
# With Python 3, you can assign variables from lists in a much more succinct way.
# Create variables first, middle and last from the given list using destructuring
# assignment (check the Resources tab for some examples), where:
# first ➞ 1
# middle ➞ [2, 3, 4, 5]
# last ➞ 6
# Your task is to unpack the list writeyourcodehere into three variables, being
# fi t iddl d l t ith iddl b i thi i b t th fi t

writeyourcodehere = [1, 2, 3, 4, 5, 6]
result=[]
first, *middle, last = writeyourcodehere
print(first)   
print(middle)  
print(last) 