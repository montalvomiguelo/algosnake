from functools import cache


def minPathSum(grid):
    @cache
    def dp(row, col):
        if row + col == 0:
            return grid[0][0]

        ans = float("inf")
        if row > 0:
            ans = min(ans, dp(row - 1, col))
        if col > 0:
            ans = min(ans, dp(row, col - 1))

        return grid[row][col] + ans

    m = len(grid)
    n = len(grid[0])
    return dp(m - 1, n - 1)


print(minPathSum([[1, 2, 3], [4, 5, 6]]))
