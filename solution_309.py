from functools import cache


def maxProfit(prices):
    @cache
    def dp(i, holding):
        if i == len(prices):
            return 0

        ans = dp(i + 1, holding)
        if holding:
            ans = max(ans,
                      prices[i] + dp(min(i + 2, len(prices)), False))
        else:
            ans = max(ans,
                      -prices[i] + dp(i + 1, True))

        return ans

    return dp(0, False)


print(maxProfit([1, 2]))
