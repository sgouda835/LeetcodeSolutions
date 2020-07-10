'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

'''

def merge(intervals):
    intervals.sort(key = lambda x : x[0])
    ans = []
    for i in intervals:
        if ans and i[0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], i[1])
        else:
            ans.append(i)
    return ans







intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))