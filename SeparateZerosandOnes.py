import scipy.special as s
def separatezerosandones(nums):
    return ([x for x in nums if x == 0] +
            [x for x in nums if x == 1])


nums =[1,0,1,0,1,0,0,0,1]
print(separatezerosandones(nums))