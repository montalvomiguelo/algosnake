from collections import defaultdict


def maximalNetworkRank(n, roads):
    graph = defaultdict(set)
    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            curr = len(graph[i]) + len(graph[j])
            if j in graph[i]:
                curr -= 1
            ans = max(ans, curr)
    return ans


print(maximalNetworkRank(8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]))
