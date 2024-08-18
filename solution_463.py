def islandPerimeter(grid):
    def valid(row, col):
        return (0 <= row < m and
                0 <= col < n and
                grid[row][col] == 1)

    def dfs(row, col):
        ans = 0
        for dx, dy in directions:
            nextRow, nextCol = row + dx, col + dy
            if not valid(nextRow, nextCol):
                ans += 1
            elif not (nextRow, nextCol) in seen:
                seen.add((nextRow, nextCol))
                ans += dfs(nextRow, nextCol)

        return ans

    seen = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    m = len(grid)
    n = len(grid[0])
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1:
                seen.add((row, col))
                return dfs(row, col)


print(islandPerimeter([[1, 1], [1, 1]]))
