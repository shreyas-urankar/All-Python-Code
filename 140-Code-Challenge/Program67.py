# Hamming distance is the number of characters that differ between two strings.
# To illustrate:
# String1: "abcbba"
# String2: "abcbda"
# Hamming Distance: 1 - "b" vs. "d" is the only difference.
# Create a function that computes the hamming distance between two strings.
# Examples
# hamming_distance("abcde", "bcdef") ➞ 5
# hamming_distance("abcde", "abcde") ➞ 0
# hamming_distance("strong", "strung") ➞ 1

def Hamming_Distance(str1, str2):
    if len(str1) != len(str2):
        print("Input strings must have the same length")
    distance=0


    unique_to_str1 = set(str1) - set(str2)
    unique_to_str2 = set(str2) - set(str1)

    if unique_to_str1:
        print(f"Letters not present in the second string: {', '.join(unique_to_str1)}")
    if unique_to_str2:
        print(f"Letters not present in the first string: {', '.join(unique_to_str2)}")


    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            distance+=1
    return distance

str1=input("Enter the first string:")
str2 = input("Enter the second string:")

try:
    result=Hamming_Distance(str1, str2)
    print(f"The Hamming distance is: {result}")
except ValueError as e:
    print(e)