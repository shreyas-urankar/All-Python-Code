# Create a function that takes three arguments a, b, c and returns the sum of the
# numbers that are evenly divided by c from the range a, b inclusive.
# Examples
# evenly_divisible(1, 10, 20) ➞ 0
# # No number between 1 and 10 can be evenly divided by 20.
# evenly_divisible(1, 10, 2) ➞ 30
# # 2 + 4 + 6 + 8 + 10 = 30
# evenly_divisible(1, 10, 3) ➞ 18
# # 3 + 6 + 9 = 18
class ED:
    def __init__(self):
        pass
    def e_d(self,a,b,c):
        total=0
        for num in range(a, b+1):
            if num%c==0:
                total +=num
        return total

e=ED()

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

result=e.e_d(a,b,c)
print(f"The sum of the numbers that are evenly divided by {c} from the range {a}, {b} inclusive is:{result}") 

    