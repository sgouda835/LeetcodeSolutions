def twoSum(nums, target):
    if len(nums) < 1:
        return False
    
    dict1 = {}
    for i in range(len(nums)):
        diff = target - nums[i]
       

        if diff in dict1:
            return dict1[diff], i
        else:
            dict1[nums[i]] = i  


nums = [2, 7, 11, 15] 
target = 9
print(list(twoSum(nums, target)))