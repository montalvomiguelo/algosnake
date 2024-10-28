from collections import Counter


def findLucky(arr):
    counts = Counter(arr)
    ans = -1

    for key, val in counts.items():
        if key == val:
            ans = max(ans, val)

    return ans
