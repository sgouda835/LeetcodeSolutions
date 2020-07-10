'''Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''

def longestPalindrome(s: str):
    def helper(l,r):
        while (l>= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return s[l+1:r]
    res = ""
    for i in range(len(s)):
        test = helper(i,i)
        if len(test) > len(res):
            res = test
        test = helper(i, i+1)
        if len(test) > len(res):
            res = test
    return res


s = "babad"
print(longestPalindrome(s))