def lengthOfLongestSubstring(s: str) -> int:
    # start = 0
    # maxlen = 0
    # lookup = {}

    # for index , character in enumerate(s):
    #     if character in lookup and start <= lookup[character]:
    #         start =  lookup[character] + 1
    #     else:
    #         maxlen = max(maxlen, index - start + 1)
    #     lookup[character] = index
    
    # return maxlen

    # if len(s) == 0:
    #     return 0
    
    # map = {}
    # max_len = start = 0

    # for i in range(len(s)):
    #     if s[i] in map and start <= map[s[i]]:
    #         start = map[s[i]] + 1
    #     else:
    #         max_len = max(max_len, i - start + 1)
    #     map[s[i]] = i
    
    # return max_len

    if len(s) == 0:
        return 0

    lookup = {}
    start = max_len = 0

    for index, character in enumerate(s):
        if character in lookup and start <= lookup[character]:
            start = lookup[character] + 1
        else:
            max_len = max(max_len, index - start + 1)
        lookup[character] = index
    
    return max_len
 
    
s = "pwwkew"
print(lengthOfLongestSubstring(s))