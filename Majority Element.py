#from collections import Counter
def majorityElement(nums):
    #return sorted(nums)[len(nums)//2]
    #return Counter(nums).most_common(1)[0][0]
    nums.sort()
    return nums[len(nums)//2]


nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))




