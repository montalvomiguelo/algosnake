import re

with open('aoc_24_07.txt') as f:
    lines = [l.rstrip('\n') for l in f]

# Part 1
data = [list(map(int, re.findall(r'\d+', l))) for l in lines]

def backtrack(curr, i, target, nums):
    if i == len(nums):
        return curr == target

    for j in range(i, len(nums)):
        if backtrack(curr + nums[j], j + 1, target, nums):
            return True

        if backtrack(curr * nums[j], j + 1, target, nums):
            return True

    return False

ans = 0
for nums in data:
    if backtrack(nums[1], 1, nums[0], nums[1:]):
        ans += nums[0]

print(ans)
        ans += nums[0]

print(ans)
