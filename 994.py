from collections import deque


def orangesRotting(grid):
    def valid(row, col):
        return 0 <= row < n and 0 <= col < m and grid[row][col] == 1

    n = len(grid)
    m = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    freshOranges = 0
    ans = 0

    for row in range(n):
        for col in range(m):
            if grid[row][col] == 2:
                queue.append((row, col, 0))
            elif grid[row][col] == 1:
                freshOranges += 1

    while queue:
        row, col, steps = queue.popleft()
        grid[row][col] = -1

        for dx, dy in directions:
            nextRow, nextCol = row + dy, col + dx
            if valid(nextRow, nextCol):
                queue.append((nextRow, nextCol, steps + 1))
                grid[nextRow][nextCol] = 2
                freshOranges -= 1

        ans = max(ans, steps)

    return -1 if freshOranges else ans


print(orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
