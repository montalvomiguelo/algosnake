def findTargetSumWays(nums, target):
    total = sum(nums)
    n = len(nums)
    dp = [[0] * (2 * total + 1) for _ in range(n)]

    dp[0][nums[0] + total] += 1
    dp[0][-nums[0] + total] += 1

    for i in range(1, n):
        for curr in range(-total, total + 1):
            if dp[i - 1][curr + total] > 0:
                dp[i][curr + nums[i] + total] += dp[i - 1][curr + total]
                dp[i][curr - nums[i] + total] += dp[i - 1][curr + total]

    return (dp[n - 1][target + total]
            if abs(target) <= total else 0)


print(findTargetSumWays([1, 1, 1, 1], 2))
