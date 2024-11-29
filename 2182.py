import heapq
from collections import Counter


def repeatLimitedString(s, repeatLimit):
    counts = Counter(s)
    heap = [(-ord(char), char) for char in counts]
    heapq.heapify(heap)
    ans = []
    while heap:
        _, char = heapq.heappop(heap)
        limit = min(counts[char], repeatLimit)
        for _ in range(limit):
            ans.append(char)
            counts[char] -= 1

        if counts[char] and heap:
            _, nextChar = heapq.heappop(heap)
            ans.append(nextChar)
            counts[nextChar] -= 1

            heapq.heappush(heap, (-ord(char), char))

            if counts[nextChar]:
                heapq.heappush(heap, (-ord(nextChar), nextChar))

    return "".join(ans)


print(repeatLimitedString("aababab", 2))
