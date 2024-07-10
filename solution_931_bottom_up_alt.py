def minFallingPathSum(matrix):
    n = len(matrix)
    dp = matrix[0][:]

    for row in range(1, n):
        nextRow = [0] * n
        for col in range(n):
            ans = dp[col]
            if col > 0:
                ans = min(ans, dp[col - 1])
            if col < n - 1:
                ans = min(ans, dp[col + 1])
            nextRow[col] = matrix[row][col] + ans
        dp = nextRow

    return min(dp)


print(minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
