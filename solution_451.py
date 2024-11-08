from collections import Counter


def frequencySort(s):
    counts = Counter(s)
    sortedCounts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    ans = []
    for key, val in sortedCounts:
        ans.append(val * key)

    return "".join(ans)
