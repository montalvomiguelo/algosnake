from collections import defaultdict


def getAncestors(n, edges):
    def dfs(node, seen):
        if node in seen:
            return

        seen.add(node)

        for nei in graph[node]:
            dfs(nei, seen)

    graph = defaultdict(list)
    for a, b in edges:
        graph[b].append(a)

    ans = []
    for i in range(n):
        path, seen = [], set()
        dfs(i, seen)
        for j in range(n):
            if j in seen and i != j:
                path.append(j)

        ans.append(path)

    return ans


print(getAncestors(8, [[0, 3], [0, 4], [1, 3], [
      2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]))
