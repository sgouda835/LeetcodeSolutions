def separate_even_odd(nums):
    return ([x for x in nums if x % 2 == 0] +
            [x for x in nums if x % 2 == 1])


nums =[1,2,3,4,5,6,7,8,9,10]
print(separate_even_odd(nums))