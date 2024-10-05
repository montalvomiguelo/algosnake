from collections import defaultdict
import re

with open('day_02.txt') as f:
    lines = [l.strip('\n') for l in f]

# Part 1
dic = {'red': 12, 'green': 13, 'blue': 14}
ans = 0
for l in lines:
    id = int(re.search(r'(\d+):', l).group(1))
    ans += id
    matches = re.findall(r'(\d+)\s+(\w+)', l)
    for match in matches:
        count, color = match
        if int(count) > dic[color]:
            ans -= id
            break

print(ans)

# Part 2
ans = 0
for l in lines:
    dic = defaultdict(int)
    matches = re.findall(r'(\d+)\s+(\w+)', l)
    res = 1
    for count, color in matches:
        dic[color] = max(dic[color], int(count))

    for v in dic.values():
        res *= v

    ans += res

print(ans)
