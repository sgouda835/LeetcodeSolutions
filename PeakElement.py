def findPeakElement(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2

        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return l


nums = [1,2,3,1]
print(findPeakElement(nums))
