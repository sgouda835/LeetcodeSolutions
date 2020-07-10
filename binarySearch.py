def binarysearch(nums, left, right, x):
    
    if right >= left:
        mid = (left + right)//2

        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            return binarysearch(nums, left, mid-1,x)
        else:
            return binarysearch(nums, mid+1 , right, x)
    else:
        return -1

nums = [1,2,3,4,5,6,7,8,9]
x = 9
n = len(nums) - 1
result = binarysearch(nums,0,n,x )
if result != -1:
    print ("Element is present at index %d" % result)
else:
    print ("Element is not present in array")
