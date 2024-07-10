from functools import cache


def minFallingPathSum(matrix):
    @cache
    def dp(row, col):
        if row == 0:
            return matrix[row][col]

        ans = dp(row - 1, col)
        if col > 0:
            ans = min(ans, dp(row - 1, col - 1))
        if col < n - 1:
            ans = min(ans, dp(row - 1, col + 1))

        return matrix[row][col] + ans

    ans = float("inf")
    n = len(matrix)
    for i in range(n):
        ans = min(ans, dp(n - 1, i))

    return ans


print(minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
