from collections import defaultdict


def equationsPossible(equations):
    def dfs(node, component):
        seen[node] = component

        for nei in graph[node]:
            if not nei in seen:
                dfs(nei, component)

    graph = defaultdict(list)
    for equation in equations:
        x, y, rel = equation[0], equation[3], equation[1]
        if rel == '=':
            graph[x].append(y)
            graph[y].append(x)

    seen = defaultdict(int)
    component = 1
    for node in graph:
        if not node in seen:
            dfs(node, component)
            component += 1

    for equation in equations:
        x, y, rel = equation[0], equation[3], equation[1]
        if rel == '!':
            if x == y:
                return False
            if not seen[x] and not seen[y]:
                continue
            if seen[x] == seen[y]:
                return False

    return True
