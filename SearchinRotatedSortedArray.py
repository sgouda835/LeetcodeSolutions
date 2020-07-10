def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right)// 2
        if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
            left = mid + 1
        else:
            right = mid

    return left if target in nums[left:left + 1] else -1 


nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))