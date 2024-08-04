def pathSum(root, targetSum):
    def dfs(node, curr):
        if not node:
            return

        curr.append(node.val)

        if not node.left and not node.right:
            if sum(curr) == targetSum:
                ans.append(curr[:])
        else:
            dfs(node.left, curr)
            dfs(node.right, curr)

        curr.pop()

    ans = []
    dfs(root, [])
    return ans
