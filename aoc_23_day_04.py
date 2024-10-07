import re


with open('day_04.txt') as f:
    lines = [l.strip('\n') for l in f]

# Part 1
ans = 0
for l in lines:
    matches = re.search(r'(\d+(?:\s+\d+)*)\s+\|\s*(\d+(?:\s+\d+)*)', l)
    numbersSet = set(matches.group(1).split())
    res, count = 1, 0
    for number in matches.group(2).split():
        if number in numbersSet:
            res *= 1 if count == 0 else 2
            count += 1

    if count:
        ans += res

print(ans)
