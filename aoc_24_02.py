import re

with open('aoc_24_02.txt') as f:
    lines = [l.rstrip('\n') for l in f]

# Part 1
data = []
for l in lines:
    matches = re.findall(r'\d+', l)
    data.append([int(num) for num in matches])

ans = 0
for nums in data:
    sorting = ''
    for i in range(len(nums) - 1):
        j = i + 1
        if nums[i] == nums[j]:
            break

        diff = abs(nums[i] - nums[j])
        if diff < 1 or diff > 3:
            break

        newSorting = 'asc' if nums[i] < nums[j] else 'dec'
        if not sorting:
            sorting = newSorting
            continue

        if newSorting != sorting:
            break

        ans += 1 if j == len(nums) - 1 else 0

print(ans)

# Part 2
def isSafe(nums):
    sorting = ''
    for i in range(len(nums) - 1):
        j = i + 1
        if nums[i] == nums[j]:
            return False

        diff = abs(nums[i] - nums[j])
        if diff < 1 or diff > 3:
            return False

        newSorting = 'asc' if nums[i] < nums[j] else 'dec'
        if not sorting:
            sorting = newSorting
            continue

        if newSorting != sorting:
            return False

    return True


ans = 0
for nums in data:
    if isSafe(nums):
        ans += 1
        continue
    for i in range(len(nums)):
        if isSafe(nums[:i] + nums[i + 1:]):
            ans += 1
            break

print(ans)
