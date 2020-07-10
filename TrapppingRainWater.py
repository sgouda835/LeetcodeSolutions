def findWater(height):
    L, R = 0, len(height) - 1
    L_max, R_max = 0, 0
    result = 0
    while L < R:
        L_max = max(L_max, height[L])
        R_max = max(R_max, height[R])
        if L_max <= R_max:
            result += L_max - height[L]
            L += 1
        else:
            result += R_max - height[R]
            R -= 1
    return result



arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print("Maximum water that can be accumulated is: ",
      findWater(arr))