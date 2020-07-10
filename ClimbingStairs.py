'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

'''
def climbStairs(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


n = 2
print(climbStairs(n))
