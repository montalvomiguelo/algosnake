from functools import cache


def canJump(nums):
    @cache
    def dp(i):
        if i == n - 1:
            return True

        ans = False

        if i >= n:
            return ans

        if nums[i] == 0:
            return ans

        for j in range(i, i + nums[i]):
            ans = dp(j + 1)
            if ans:
                return ans

        return ans

    n = len(nums)
    return dp(0)


print(canJump([2, 0]))
