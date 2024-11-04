import heapq


def findContentChildren(g, s):
    ans = 0
    if not s:
        return ans

    g.sort()
    heapq.heapify(s)

    for i in range(len(g)):
        if not s:
            break

        while s:
            size = heapq.heappop(s)
            if size >= g[i]:
                ans += 1
                break

    return ans


print(findContentChildren([7, 8, 9, 10], [5, 6, 7, 8]))
