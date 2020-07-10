def isrotation(s1, s2):
    return len(s1) == len(s2) and s1 in 2 * s2

s1 = "santosh"
s2 = "antoshs"

print(isrotation(s1,s2))