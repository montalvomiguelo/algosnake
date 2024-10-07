from functools import cache
import re


with open('day_04.txt') as f:
    lines = [l.strip('\n') for l in f]

# Part 1
ans = 0
for l in lines:
    match = re.search(r'(\d+(?:\s+\d+)*)\s+\|\s+(\d+(?:\s+\d+)*)', l)
    winningNumbers = set(match.group(1).split())
    numbers = match.group(2).split()
    res, count = 1, 0
    for number in numbers:
        if number in winningNumbers:
            res *= 1 if count == 0 else 2
            count += 1

    if count:
        ans += res

print(ans)

# Part 2


@cache
def dp(i):
    l = lines[i]
    match = re.search(r'(\d+(?:\s+\d+)*)\s+\|\s+(\d+(?:\s+\d+)*)', l)
    winningNumbers = set(match.group(1).split())
    numbers = match.group(2).split()
    ans, j = 1, 1
    for number in numbers:
        if number in winningNumbers:
            ans += dp(i + j)
            j += 1
    return ans


ans = 0
for i in range(len(lines)):
    ret = dp(i)
    ans += ret

print(ans)
