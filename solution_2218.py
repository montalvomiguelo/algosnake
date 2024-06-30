from functools import cache


def maxValueOfCoins(piles, k):
    @cache
    def dp(i, remain):
        if i == len(piles) or remain == 0:
            return 0

        ans = dp(i + 1, remain)  # skip this pile
        curr = 0
        # make sure we don't take more coins than we are allowed to
        for j in range(min(remain,
                           len(piles[i]))):
            curr += piles[i][j]
            ans = max(ans,
                      curr + dp(i + 1, remain - j - 1))

        return ans

    return dp(0, k)


print(maxValueOfCoins([[1, 100, 3], [7, 8, 9]], 2))
