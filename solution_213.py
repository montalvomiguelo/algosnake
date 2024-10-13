from functools import cache


def rob(nums):
    @cache
    def dp(i, j):
        if i == j:
            return nums[j]

        if i == j + 1:
            return max(nums[j], nums[j + 1])

        return max(dp(i - 1, j), nums[i] + dp(i - 2, j))

    n = len(nums)
    if n == 1:
        return nums[0]

    return max(dp(n - 1, 1), dp(n - 2, 0))


print(rob([2, 3, 2]))
