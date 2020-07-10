def firstOccurance(nums,x):
    for i in range(len(nums)):
        if nums[i] == x:
            return i


nums =[1,2,2,3,4,5,6,6,6]
x = 2
print(firstOccurance(nums , x))