from collections import defaultdict


def getAncestors(n, edges):
    def dfs(node, path, seen):
        if node in seen:
            return

        path.append(node)
        seen.add(node)

        for nei in graph[node]:
            dfs(nei, path, seen)

    graph = defaultdict(list)
    for a, b in edges:
        graph[b].append(a)

    ans = []
    for i in range(n):
        path, seen = [], set()
        dfs(i, path, seen)
        ans.append(sorted(path[1:]))

    return ans


print(getAncestors(8, [[0, 3], [0, 4], [1, 3], [
      2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]))
