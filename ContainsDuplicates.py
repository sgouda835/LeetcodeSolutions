def containsDuplicate(nums):
    if len(nums) != len(set(nums)):
        return True
    return False

nums = [1,2,3,4,5,6,1]
print(containsDuplicate(nums))