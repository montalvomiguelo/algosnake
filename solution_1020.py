def numEnclaves(grid):
    def valid(row, col):
        return 0 <= row < m and 0 <= col < n

    def dfs(row, col):
        ans = 1
        seen.add((row, col))
        invalidCount = 0

        for dx, dy in directions:
            nextRow, nextCol = dx + row, dy + col
            if not valid(nextRow, nextCol):
                invalidCount += 1
                continue

            if (grid[nextRow][nextCol] == 0 or
                (nextRow, nextCol) in seen):
                continue

            ret = dfs(nextRow, nextCol)
            if not ret:
                invalidCount += 1
                continue

            ans += ret

        return ans if not invalidCount else 0

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    m = len(grid)
    n = len(grid[0])
    seen = set()
    ans = 0
    for row in range(m):
        for col in range(n):
            if ((row, col) not in seen and
                grid[row][col] == 1):
                ans += dfs(row, col)

    return ans


print(numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
