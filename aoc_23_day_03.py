from collections import defaultdict
import re


with open('day_03.txt') as f:
    matrix = [l.strip('\n') for l in f]

m = len(matrix)
n = len(matrix[0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, 1), (-1, -1), (1, 1), (1, -1)]


def valid(row, col):
    return 0 <= row < m and 0 <= col < n


# Part 1
ans = 0
for row in range(m):
    number, symbol = '', ''
    for col in range(n):
        if matrix[row][col].isdigit():
            number += matrix[row][col]
            for dx, dy in directions:
                nextRow, nextCol = dx + row, dy + col
                if valid(nextRow, nextCol) and not re.match(r'[\d.]', matrix[nextRow][nextCol]):
                    symbol = matrix[nextRow][nextCol]
        else:
            if symbol:
                ans += int(number)
            number, symbol = '', ''
        if col == n - 1 and symbol:
            ans += int(number)

print(ans)

# Part 2
dic = defaultdict(list)
for row in range(m):
    number, key = '', None
    for col in range(n):
        if matrix[row][col].isdigit():
            number += matrix[row][col]
            for dx, dy in directions:
                nextRow, nextCol = dx + row, dy + col
                if valid(nextRow, nextCol) and matrix[nextRow][nextCol] == '*':
                    key = [nextRow, nextCol]
        else:
            if key:
                dic[tuple(key)].append(int(number))
            number, key = '', None
        if col == n - 1 and key:
            dic[tuple(key)].append(int(number))

ans = 0
for k, v in dic.items():
    if len(v) == 2:
        ans += v[0] * v[1]

print(ans)
