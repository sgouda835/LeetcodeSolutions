import sys
def maxSum(arr, n, k):
    # if not n > k:
    #     print("Invalid")
    #     return -1
    max_sum = -sys.maxsize - 1
    window_sum = sum([arr[i] for i in range(k)])

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    return max_sum

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, len(arr), k))
