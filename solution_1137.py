from functools import cache


def tribonacci(n):
    @cache
    def dp(n):
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        return dp(n - 1) + dp(n - 2) + dp(n - 3)

    return dp(n)


print(tribonacci(25))
