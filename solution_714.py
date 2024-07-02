from functools import cache


def maxProfit(prices, fee):
    @cache
    def dp(i, holding):
        if i == len(prices):
            return 0

        ans = dp(i + 1, holding)
        if holding:
            ans = max(ans,
                      prices[i] + dp(i + 1, False) - fee)
        else:
            ans = max(ans,
                      -prices[i] + dp(i + 1, True))

        return ans

    return dp(0, False)


print(maxProfit([1, 3, 2, 8, 4, 9], 2))
