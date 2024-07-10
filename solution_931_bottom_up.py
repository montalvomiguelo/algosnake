def minFallingPathSum(matrix):
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[0][i] = matrix[0][i]

    for row in range(n):
        for col in range(n):
            if row == 0:
                continue

            ans = dp[row - 1][col]
            if col > 0:
                ans = min(ans, dp[row - 1][col - 1])
            if col < n - 1:
                ans = min(ans, dp[row - 1][col + 1])

            dp[row][col] = matrix[row][col] + ans

    ans = float("inf")
    for i in range(n):
        ans = min(ans, dp[n - 1][i])

    return ans


print(minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
