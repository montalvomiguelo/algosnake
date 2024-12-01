import re

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
