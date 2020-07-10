'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

def groupAnagrams(strs):
    dict = {}
    for word in strs:
        sortedword = "".join(sorted(word))
        if sortedword not in dict:
            dict[sortedword] = [word]
        else:
            dict[sortedword].append(word)
    
    result = []
    for item in dict.values():
        result.append(item)
    return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))