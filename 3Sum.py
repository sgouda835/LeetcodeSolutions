def threeSum(array):
    array.sort()
    output = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1 
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == 0:
                output.append([array[i] , array[left] , array[right]])
                left += 1
                right -= 1
            elif currentSum < 0:
                left += 1
            elif currentSum > 0:
                right -= 1
    
    return list(output)

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))