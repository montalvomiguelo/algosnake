import re
from collections import defaultdict

with open('aoc_24_05.txt') as f:
    sections = f.read().strip().split('\n\n')

# Part 1
rules = sections[0].split('\n')
updates = [[int(n) for n in l.split(',')] for l in sections[1].split('\n')]
graph = defaultdict(list)
for rule in rules:
    a, b = re.findall(r'\d+', rule)
    graph[int(a)].append(int(b))

validUpdates = []
for update in updates:
    seen = set()
    valid = True
    for page in update:
        if not valid:
            break

        seen.add(page)
        for nei in graph[page]:
            if nei in seen:
                valid = False
                break

    if valid:
        validUpdates.append(update)

ans = 0
for update in validUpdates:
    ans += update[len(update) // 2]

print(ans)

# Part 2
invalidUpdates = []
for update in updates:
    seen = set()
    valid = True
    for page in update:
        if not valid:
            break

        seen.add(page)
        for nei in graph[page]:
            if nei in seen:
                valid = False
                break

    if not valid:
        invalidUpdates.append(update)

for update in invalidUpdates:
    n = len(update)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if update[j] in graph[update[j + 1]]:
                update[j], update[j + 1] = update[j + 1], update[j]

ans = 0
for update in invalidUpdates:
    ans += update[len(update) // 2]

print(ans)
