from collections import Counter

def isAnagram(string1, string2):
    if Counter(string1) == Counter(string2):
        return "Anagram"
    else:
        return "Not Anagram"

s1 = "silent"
s2 = "listen"
print(isAnagram(s1,s2))