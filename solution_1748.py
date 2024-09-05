from collections import Counter

def sumOfUnique(nums):
    counts = Counter(nums)
    ans = 0
    for key, val in counts.items():
        if val == 1:
            ans += key

    return ans


print(sumOfUnique([1, 2, 3, 2]))
