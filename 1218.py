from functools import cache


def longestSubsequence(arr, difference):
    @cache
    def dp(i):
        ans = 1

        for j in range(i):
            if arr[i] - arr[j] == difference:
                ans = max(ans, dp(j) + 1)

        return ans

    return max(dp(i) for i in range(len(arr)))


print(longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))
