import statistics

def elementwithmaxtimes(nums):
    return statistics.mode(nums)


nums = [1,2,3,4,4,4,4,5,3,2,1]
print(elementwithmaxtimes(nums))