import re
from collections import Counter

with open('aoc_24_01.txt') as f:
    lines = [l.rstrip('\n') for l in f]

# Part 1
left = []
right = []
for l in lines:
    matches = re.findall(r'(\d+)\s+(\d+)', l)
    for match in matches:
        x, y = match
        left.append(int(x))
        right.append(int(y))

left.sort()
right.sort()
diffs = []
for i in range(len(left)):
    x = left[i]
    y = right[i]
    diffs.append(abs(x - y))

print(sum(diffs))

# Part 2
dic = Counter(right)
ans = 0
for x in left:
    y = dic[x]
    ans += y * x if y else 0

print(ans)
