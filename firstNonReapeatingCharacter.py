# def firstNonreapeatingCharacter(s):
#     return [a for a in s if s.count(a) == 1][0]
#
#
# s = "santosh"
# print(firstNonreapeatingCharacter(s))


import collections

def firstNonreapeatingCharacter(s):
    count = collections.Counter(s)
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return ch
    return -1

s = "geeksforgeeks"
print(firstNonreapeatingCharacter(s))