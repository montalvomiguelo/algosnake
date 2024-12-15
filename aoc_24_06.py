with open('aoc_24_06.txt') as f:
    grid = [list(s) for s in [l.rstrip('\n') for l in f]]

# Part 1
def valid(row, col):
    return 0 <= row < n and 0 <= col < m

n = len(grid)
m = len(grid[0])
curr = (-1, -1)
seen = set()
for row in range(n):
    for col in range(m):
        if grid[row][col] == '^':
            curr = (row, col)
            seen.add(curr)
            break

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
i = 0
while True:
    dy, dx = directions[i]
    nextRow, nextCol = curr[0] + dy, curr[1] + dx
    if not valid(nextRow, nextCol):
        break

    if grid[nextRow][nextCol] != '#':
        curr = (nextRow, nextCol)
        seen.add((curr))
        continue

    i = (i + 1) % 4
    dy, dx = directions[i]
    nextRow, nextCol = curr[0] + dy, curr[1] + dx
    if valid(nextRow, nextCol):
        curr = (nextRow, nextCol)
        seen.add(curr)

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
        seen = [[[0] * 4 for _ in range(m)] for _ in range(n)]
        i = 0
        while True:
            if seen[curr[0]][curr[1]][i]:
                ans += 1
                break

            seen[curr[0]][curr[1]][i] = 1

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
