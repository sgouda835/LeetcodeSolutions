import collections
def duplicate(nums):
    return [item for item, count in collections.Counter(nums).items() if count > 1]
 
nums = [1,2,3,4,5,5,6,1,2,2]
print(duplicate(nums))
