def longestSubsequence(arr, difference):
    def dp(a):
        memo[a] = memo.get(a - difference, 0) + 1
        return memo[a]

    memo = {}
    return max(dp(a) for a in arr)


print(longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))
