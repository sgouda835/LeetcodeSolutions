def elementtwiceinarray(nums):
    res = []
    for x in nums:
        if nums[abs(x) - 1] < 0:
            res.append(abs(x))
        else:
            nums[abs(x) - 1] *= -1
    return res


nums = [1,2,3,4,5,4,6,7,7,6]
print(elementtwiceinarray(nums))