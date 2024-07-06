def uniquePaths(m, n):
    dp = [0] * n
    dp[0] = 1

    for _ in range(m):
        nextRow = [0] * n
        for col in range(n):
            nextRow[col] += dp[col]
            if col > 0:
                nextRow[col] += nextRow[col - 1]

        dp = nextRow

    return dp[n - 1]


print(uniquePaths(3, 2))
