def maxArea(height):
    max_area = 0
    temp_area = 0
    left = 0
    right = len(height) - 1

    for i in range(len(height)):
        width = right - left

        if height[left] < height[right]:
            temp_area = width * height[left]
            left += 1
        
        else:
            temp_area = width * height[right]
            right -= 1
        max_area = max(max_area,temp_area)
    
    return max_area


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))