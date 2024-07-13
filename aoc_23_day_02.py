import re

with open('day_02.txt') as f:
    lines = [l.strip('\n') for l in f]
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
