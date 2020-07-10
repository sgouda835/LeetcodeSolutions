def maximumdiffernce(nums, n):
    max_diff = 0
    min = nums[0]

    for i in range(n):
        if (nums[i] - min) > max_diff:
            max_diff = nums[i]-min

        if nums[i] < min:
            min = nums[i]
            
    print("max Difference:",max_diff)


nums = [1, 2, 90, 10, 110]
n = len(nums)
maximumdiffernce(nums,n)