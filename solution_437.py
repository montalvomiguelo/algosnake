from collections import defaultdict


def pathSum(root, targetSum):
    def dfs(node, curr):
        nonlocal ans
        if not node:
            return

        curr += node.val
        if curr == targetSum:
            ans += 1

        ans += counts[curr - targetSum]
        counts[curr] += 1

        dfs(node.left, curr)
        dfs(node.right, curr)

        counts[curr] -= 1

    ans = 0
    counts = defaultdict(int)
    dfs(root, 0)
    return ans
