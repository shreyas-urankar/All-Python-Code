# Write a Python Program to Find LCM.
# Least Common Multiple (LCM):
# LCM, or Least Common Multiple, is the smallest multiple that is exactly divisible by two or
# more numbers.
# Formula:
# For two numbers a and b, the LCM can be found using the formula:
# For more than two numbers, you can find the LCM step by step, taking the LCM of pairs of
# numbers at a time until you reach the last pair.
# Note: GCD stands for Greatest Common Divisor.
# LCM(𝑎, 𝑏) =|𝑎 ⋅ 𝑏|
#         GCD(𝑎, 𝑏)

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
maxNum=max(num1, num2)
while(True):
    if(maxNum%num1==0 and maxNum%num2==0):
        break
    maxNum=maxNum+1
print(f"The LCM of {num1} and {num2} is {maxNum}.")
