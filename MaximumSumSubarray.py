def maxSubArray(nums):
    maxsum, currentsum = nums[0], nums[0]
    for i in nums[1:]:
        currentsum = max(i, currentsum + i)
        maxsum = max(maxsum, currentsum)
    return maxsum


arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print(maxSubArray(arr))