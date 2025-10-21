    def dfs(node, currentSum, path):
        if not node:
            return

        currentSum += node.val
        path.append(node.val)

        # Check if it's a leaf node and the path sum equals target sum
        if not node.left and not node.right and currentSum == targetSum:
            result.append(list(path))
        else:
            dfs(node.left, currentSum, path)
            dfs(node.right, currentSum, path)

        # Backtrack
        path.pop()

    result = []
    dfs(root, 0, [])
    return result

# review 2025-07-21

# review 2025-10-21
