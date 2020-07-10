def leaderofanarray(nums , n):
    max_from_right = nums[n - 1]
    print(max_from_right,end=" ")

    for i in range(n - 2, -1, -1):
        if max_from_right < nums[i]:
            print(nums[i], end=" ")
            max_from_right = nums[i]


nums = [16, 17, 4, 3, 5, 2]
leaderofanarray(nums, len(nums))
