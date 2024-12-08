import re

with open('aoc_24_03.txt') as f:
    line = f.read().strip()

# Part 1
ans = 0
matches = re.findall(r'mul\((\d+),(\d+)\)', line)
for a, b in matches:
    ans += int(a) * int(b)

print(ans)

# Part 2
ans = 0
enabled = True
matches = re.findall(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))', line)
for match in matches:
    if match[3]:
        enabled = False
        continue

    if match[2]:
        enabled = True
        continue

    if not enabled:
        continue

    ans += int(match[0]) * int(match[1])

print(ans)
