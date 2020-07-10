from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


s = "rat"
t = "cat"
print(isAnagram(s,t))