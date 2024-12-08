import re

with open('aoc_24_04.txt') as f:
    grid = [l.strip('\n') for l in f]

# Part 1
def valid(row, col):
    return 0 <= row < n and 0 <= col < m and grid[row][col] in validLetters

def dfs(row, col, dir, curr):
    curr.append(grid[row][col])
    if len(curr) == 4:
        word = ''.join(curr)
        return True if word == 'XMAS' or word == 'SAMX' else False

    dx, dy = directions[dir]
    nextRow, nextCol = row + dy, col + dx
    if valid(nextRow, nextCol):
        return dfs(nextRow, nextCol, dir, curr)

    return False

validLetters = set(['X', 'M', 'A', 'S'])
n = len(grid)
m = len(grid[0])
directions = [(-1, 0), (-1, -1), (-1, 1), (0, -1),
              (0, 1), (1, 0), (1, -1), (1, 1)]
ans = 0
for row in range(n):
    for col in range(m):
        if grid[row][col] == 'X':
            for i in range(len(directions)):
                ans += 1 if dfs(row, col, i, []) else 0

print(ans)

# Part 2
validLetters = set(['M', 'S'])
directions = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
ans = 0
for row in range(n):
    for col in range(m):
        if grid[row][col] == 'A':
            adjLetters = []
            for dx, dy in directions:
                nextRow, nextCol = row + dy, col + dx
                masCount = 0
                if valid(nextRow, nextCol):
                    adjLetters.append(grid[nextRow][nextCol])

                for a, b in zip(adjLetters[::2], adjLetters[1::2]):
                    word = ''.join([a, 'A', b])
                    if word == 'MAS' or word == 'SAM':
                        masCount += 1

                ans += 1 if masCount == 2 else 0

print(ans)
