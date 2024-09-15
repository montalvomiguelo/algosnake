from functools import cache


def findTargetSumWays(nums, target):
    @cache
    def dp(i, curr):
        if i == 0:
            return (
                1 if curr + nums[i] == target else 0
            ) + (
                1 if curr - nums[i] == target else 0
            )

        return dp(i - 1, curr + nums[i]) + dp(i - 1, curr - nums[i])

    return dp(len(nums) - 1, 0)


print(findTargetSumWays([0, 0, 1], 1))
