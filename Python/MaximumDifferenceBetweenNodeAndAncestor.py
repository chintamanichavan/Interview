# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildTree(values, index=0):
        # Helper function to build a tree from a list
        if index < len(values) and values[index] is not None:
            node = TreeNode(values[index])
            node.left = buildTree(values, 2 * index + 1)
            node.right = buildTree(values, 2 * index + 2)
            return node
        return None

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur_max, cur_min):
            if not node:
                return cur_max - cur_min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left_diff = dfs(node.left, cur_max, cur_min)
            right_diff = dfs(node.right, cur_max, cur_min)
            return max(left_diff, right_diff)

        return dfs(root, root.val, root.val)
