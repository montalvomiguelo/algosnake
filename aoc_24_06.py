with open('aoc_24_06.txt') as f:
    grid = [list(s) for s in [l.rstrip('\n') for l in f]]

# Part 1
def valid(row, col):
    return 0 <= row < n and 0 <= col < m

n = len(grid)
m = len(grid[0])
stack = []
seen = set()
for row in range(n):
    for col in range(m):
        if grid[row][col] == '^':
            seen.add((row, col))
            stack.append((row, col, 0))
            break

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while stack:
    row, col, i = stack.pop()
    dy, dx = directions[i]
    nextRow, nextCol = row + dy, col + dx
    if valid(nextRow, nextCol):
        if grid[nextRow][nextCol] != '#':
            seen.add((nextRow, nextCol))
            stack.append((nextRow, nextCol, i))
            continue

        i = (i + 1) % 4
        dy, dx = directions[i]
        nextRow, nextCol = row + dy, col + dx
        if valid(nextRow, nextCol):
            seen.add((nextRow, nextCol))
            stack.append((nextRow, nextCol, i))

print(len(seen))

# Part 2
root = (-1 , -1)
for row in range(n):
    for col in range(m):
        if grid[row][col] == '^':
            root = (row, col)
            break

ans = 0
for row in range(n):
    for col in range(m):
        char = grid[row][col]
        if char == '^' or char == '#':
            continue

        grid[row][col] = '#'
        curr = root
        seen = set()
        i = 0
        while True:
            if (curr[0], curr[1], i) in seen:
                ans += 1
                break

            seen.add((curr[0], curr[1], i))

            dy, dx = directions[i]
            nextRow, nextCol = curr[0] + dy, curr[1] + dx
            if not valid(nextRow, nextCol):
                break

            if grid[nextRow][nextCol] == '#':
                for j in range(1, 4):
                    k = (j + i) % 4
                    dy, dx = directions[k]
                    nextRow, nextCol = curr[0] + dy, curr[1] + dx
                    if grid[nextRow][nextCol] != '#':
                        curr = (nextRow, nextCol)
                        i = k
                        break

                continue

            curr = (nextRow, nextCol)

        grid[row][col] = char

print(ans)
