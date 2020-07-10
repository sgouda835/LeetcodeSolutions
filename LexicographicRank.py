from math import factorial as fact
def calcuLexicoRank(s, n):
    rank = 1
    for i in range(n):
        count = 0
        for j in range(i + 1, n ):
            if s[i] > s[j]:
                count += 1
        rank += count * fact(n - i)

    return rank


s = "DCBA"
n = len(s)
print(calcuLexicoRank(s, n))