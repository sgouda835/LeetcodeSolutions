# def checkDuplicate(nums):
#  data = set()
#     for i in nums:
#         if i in data:
#             return True
#         data.add(i)
#     return False

# nums = [1,2,3,4,4,5,6,7]
# print(checkDuplicate(nums))


# def checkDuplicate(nums):
#     nums.sort()

#     for i in range(1,len(nums)):
#         if nums[i] == nums[i - 1]:
#             return True
#     return False

# nums = [1,2,3,4,4,5,6,7]
# print(checkDuplicate(nums))



def checkDuplicate(nums):
    if len(nums) != len(set(nums)):
        return True
    else:
        return False


nums = [1, 2, 3, 4, 5, 6,7,7]
print(checkDuplicate(nums)) 