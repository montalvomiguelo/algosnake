def generate(numRows):
    dp = [[1]]

    for i in range(1, numRows):
        prevRow = dp[- 1]
        nextRow = [1] * (i + 1)
        for j in range(1, i):
            nextRow[j] = prevRow[j - 1] + prevRow[j]

        dp.append(nextRow)

    return dp


print(generate(5))
