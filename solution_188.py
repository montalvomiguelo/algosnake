from functools import cache


def maxProfit(k, prices):
    @cache
    def dp(i, holding, remain):
        if i == len(prices) or remain == 0:
            return 0

        ans = dp(i + 1, holding, remain)
        if holding:
            ans = max(
                ans,
                prices[i] + dp(i + 1, False, remain - 1)
            )
        else:
            ans = max(
                ans,
                -prices[i] + dp(i + 1, True, remain)
            )

        return ans

    return dp(0, False, k)


print(maxProfit(2, [3, 2, 6, 5, 0, 3]))
