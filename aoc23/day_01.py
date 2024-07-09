import re

with open('day_01.txt') as f:
    lines = [l.rstrip('\n') for l in f]
    ans = 0
    for l in lines:
        matches = re.findall(r'\d', l)
        ans += int(matches[0] + matches[-1])

    print(ans)
