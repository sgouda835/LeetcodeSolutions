def dutch_national_flag(nums):
    return [0]*nums.count(0) + [1]*nums.count(1) + [2]*nums.count(2)


nums = [0,1,2,2,0,2,1,2,2,1,0]
print(dutch_national_flag(nums))