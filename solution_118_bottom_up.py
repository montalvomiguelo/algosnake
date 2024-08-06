def generate(numRows):
    dp = [[1] * i for i in range(1, numRows + 1)]

    for i in range(1, numRows):
        prevRow = dp[i - 1]
        for j in range(1, i):
            dp[i][j] = prevRow[j - 1] + prevRow[j]

    return dp


print(generate(5))
