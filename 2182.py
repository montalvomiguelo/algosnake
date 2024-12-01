import heapq


def repeatLimitedString(s, repeatLimit):
    counts = [0] * 26
    for c in s:
        counts[ord(c) - ord("a")] += 1

    heap = [(-(i + ord("a")), chr(i + ord("a")), i)
            for i in range(26) if counts[i]]

    heapq.heapify(heap)
    ans = []
    while heap:
        _, c, i = heapq.heappop(heap)
        limit = min(counts[i], repeatLimit)
        ans.append(c * limit)
        counts[i] -= limit

        if counts[i] and heap:
            _, nc, j = heapq.heappop(heap)
            ans.append(nc)
            counts[j] -= 1

            if counts[j]:
                heapq.heappush(heap, (-ord(nc), nc, j))

            heapq.heappush(heap, (-ord(c), c, i))

    return "".join(ans)


print(repeatLimitedString("aababab", 2))
