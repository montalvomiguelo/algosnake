def deleteNode(root, key):
    def dfs(node, goLeft):
        if goLeft:
            if not node.left:
                return node.val

            return dfs(node.left, True)

        else:
            if not node.right:
                return node.val

            return dfs(node.right, False)

    if not root:
        return None

    if root.val > key:
        root.left = deleteNode(root.left, key)
    if root.val < key:
        root.right = deleteNode(root.right, key)
    if root.val == key:
        if not root.left and not root.right:
            return None

        if root.right:
            root.val = dfs(root.right, True)
            root.right = deleteNode(root.right, root.val)
        else:
            root.val = dfs(root.left, False)
            root.left = deleteNode(root.left, root.val)

    return root
