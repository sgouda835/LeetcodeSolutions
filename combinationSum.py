'''Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
'''

def combinationSum(candidates, target):
    dp = [[] for _ in range(target + 1)]
    candidates.sort()

    for c in candidates:
        for i in range(1, target + 1 ):
            if i < c:
                continue
            if i == c:
                dp[i].append([c])
            else:
                for blist in dp[i-c]:
                    dp[i].append(blist +[c])
    
    return dp[target]






candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates,target))