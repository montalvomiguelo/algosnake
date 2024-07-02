def maxProfit(prices, fee):
    n = len(prices)
    dp = [[0 for _ in range(2)] for __ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for holding in range(2):
            ans = dp[i + 1][holding]
            if holding:
                ans = max(ans, prices[i] + dp[i + 1][0] - fee)
            else:
                ans = max(ans, -prices[i] + dp[i + 1][1])

            dp[i][holding] = ans

    return dp[0][0]


print(maxProfit([1, 3, 2, 8, 4, 9], 2))
