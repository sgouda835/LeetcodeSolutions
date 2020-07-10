'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
'''
import re
def isPalindrome(s):
    s = re.sub('[^A-Za-z0-9]+',"",s)
    s = s.lower()

    return s == s[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))