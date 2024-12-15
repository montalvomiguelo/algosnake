with open('aoc_24_04.txt') as f:
    grid = [l.strip('\n') for l in f]

# Part 1
def valid(row, col):
    return 0 <= row < n and 0 <= col < m and grid[row][col]

n = len(grid)
m = len(grid[0])
directions = [(-1, 0), (-1, -1), (-1, 1), (0, -1),
              (0, 1), (1, 0), (1, -1), (1, 1)]
ans = 0
for row in range(n):
    for col in range(m):
        if grid[row][col] == 'X':
            for i in range(len(directions)):
                curr = (row, col)
                letters = ['X']
                dy, dx = directions[i]
                for _ in range(3):
                    nextRow, nextCol = dy + curr[0], dx + curr[1]
                    if not valid(nextRow, nextCol):
                        break

                    letters.append(grid[nextRow][nextCol])
                    curr = (nextRow, nextCol)

                ans += 1 if ''.join(letters) == 'XMAS' else 0

print(ans)

# Part 2
directions = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
ans = 0
for row in range(n):
    for col in range(m):
        if grid[row][col] == 'A':
            letters = []
            for dy, dx in directions:
                nextRow, nextCol = row + dy, col + dx
                if not valid(nextRow, nextCol):
                    break

                letters.append(grid[nextRow][nextCol])

            count = 0
            for a, b in zip(letters[::2], letters[1::2]):
                word = ''.join([a, 'A', b])
                if word == 'MAS' or word == 'SAM':
                    count += 1

            ans += 1 if count == 2 else 0

print(ans)
