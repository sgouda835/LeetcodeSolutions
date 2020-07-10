def maxSubArray(nums):
    maxEndingHere = maxSoFar= nums[0]
        
    for num in nums[1:]:
        maxEndingHere = max(num,maxEndingHere + num)
        maxSoFar = max(maxSoFar,maxEndingHere)
    return maxSoFar

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))