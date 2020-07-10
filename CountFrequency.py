from collections import Counter

# def frequency(nums):
#     dict ={}

#     for item in nums:
#         if item in dict:
#             dict[item] += 1
#         else:
#             dict[item] = 1

#     for key, value in dict.items():
#         print(f"{key} : {value}")

# def freq(nums):
#     c = Counter(nums)
#     print(f"{c.keys()} : {c.values()}")

from itertools import groupby
def freq(nums):
    results = {value: len(list(freq)) for value, freq in groupby(sorted(nums))}
    return (results)

nums =[1,2,3,4,5,1,2,1,2,1,6,7,8,9]
print(freq(nums))
