from collections import deque


def orangesRotting(grid):
    def valid(row, col):
        return 0 <= row < n and 0 <= col < m and grid[row][col] == 1

    n = len(grid)
    m = len(grid[0])
    queue = deque()
    freshOranges = 0
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 2:
                queue.append((row, col, 0))
            elif grid[row][col] == 1:
                freshOranges += 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ans = 0
    while queue:
        row, col, steps = queue.popleft()

        for dx, dy in directions:
            nextRow, nextCol = row + dy, col + dx
            if valid(nextRow, nextCol):
                queue.append((nextRow, nextCol, steps + 1))
                grid[nextRow][nextCol] = 2
                freshOranges -= 1

        ans = max(ans, steps)

    return ans if not freshOranges else -1


print(orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
