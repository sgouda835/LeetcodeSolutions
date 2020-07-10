import math
def arrangeCoins(n):
    return int(math.sqrt(2*n + 0.25) - 0.5)

n = 8
print(arrangeCoins(n))
