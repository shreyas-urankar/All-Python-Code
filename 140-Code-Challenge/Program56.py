#  Write a Python program to find uncommon words from two Strings.
def uncommon_words(str1, str2):
    words1=set(str1.split())
    words2=set(str2.split())
    uncommon_words_set=words1.symmetric_difference(words2) # type: ignore
    uncommon_words_list=list(uncommon_words_set)

    return uncommon_words_list

string1=input("Enter a string1:")
string2=input("Enter a string2:")
uncommon=uncommon_words(string1, string2)
print(f"Uncommon words: {uncommon}")