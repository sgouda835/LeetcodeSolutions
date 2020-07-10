def lastOccurance(nums,x):
    for i in reversed(range(len(nums))):
        if nums[i] == x:
            return i


nums =[1,2,3,4,5,6,6,6]
x = 6
print(lastOccurance(nums , x))