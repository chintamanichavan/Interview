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
        
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            nonlocal count
            if not node:
                return

            # Toggle the bit corresponding to the node's value
            path ^= 1 << node.val

            # Check if it's a leaf node
            if not node.left and not node.right:
                # Check if the path is pseudo-palindromic
                if path & (path - 1) == 0:
                    count += 1
                return

            dfs(node.left, path)
            dfs(node.right, path)

        count = 0
        dfs(root, 0)
        return count
