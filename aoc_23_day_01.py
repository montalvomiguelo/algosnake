import re

with open('day_01.txt') as f:
    lines = [l.rstrip('\n') for l in f]

ans = 0
for l in lines:
    matches = re.findall(r'\d', l)
    ans += int(matches[0] + matches[-1])

print(ans)

dic = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
       'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
ans = 0
for l in lines:
    matches = re.findall(
        r'\d|one|two|three|four|five|six|seven|eight|nine|ten', l)
    ans += int(''.join([dic[d]
               if d in dic else d for d in [matches[0], matches[-1]]]))

print(ans)
