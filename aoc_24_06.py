with open('aoc_24_06.txt') as f:
    grid = [l.rstrip('\n') for l in f]

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
