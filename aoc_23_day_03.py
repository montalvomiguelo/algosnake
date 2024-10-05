import re


with open('day_03.txt') as f:
    matrix = [l.strip('\n') for l in f]

# Part 1
m = len(matrix)
n = len(matrix[0])


def valid(row, col):
    return 0 <= row < m and 0 <= col < n and not re.match(r'(\d|\.)', matrix[row][col])


ans = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, 1), (-1, -1), (1, 1), (1, -1)]
for row in range(m):
    number = ''
    neighbors = ''
    for col in range(n):
        if matrix[row][col].isdigit():
            number += matrix[row][col]
            for dx, dy in directions:
                nextRow, nextCol = dx + row, dy + col
                if valid(nextRow, nextCol):
                    neighbors += matrix[nextRow][nextCol]
        else:
            if len(neighbors):
                ans += int(number)
            number = ''
            neighbors = ''
        if col == n - 1 and len(neighbors):
            ans += int(number)


print(ans)
