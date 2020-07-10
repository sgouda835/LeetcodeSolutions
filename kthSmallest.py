def kthsmallest(nums, k):
    nums.sort()

    return nums[len(nums) - 1 - k]


nums = [10,20,30,40,50,60]
k = 3
print(kthsmallest(nums, k))
