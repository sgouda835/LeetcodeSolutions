def getOddOccurance(nums):
    res = 0
    for index in nums:
        res = res ^ index
    return res

list1 = [1,2,3,4,4,3,3,2,1]
print(getOddOccurance(list1))