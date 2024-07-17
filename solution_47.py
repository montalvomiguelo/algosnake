from collections import Counter


def permuteUnique(nums):
    def backtrack(curr, counts):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return

        for num, freq in counts.items():
            if freq > 0:
                curr.append(num)
                counts[num] -= 1
                backtrack(curr, counts)
                curr.pop()
                counts[num] += 1

    counts = Counter(nums)
    ans = []
    backtrack([], counts)
    return ans


print(permuteUnique([1, 1, 2]))
