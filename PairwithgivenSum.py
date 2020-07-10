from itertools import combinations


def findPairs(lst, K):
    return [pair for pair in combinations(lst, 3) if sum(pair) == K]
    # dic = {}
    # for i, n in enumerate(lst):
    #     if n in dic:
    #         return [dic[n], i]
    #     dic[K - n] = i

# Driver code
lst = [1, 5, 3, 7, 9]
K = 9
print(findPairs(lst, K))