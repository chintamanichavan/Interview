# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        from collections import deque

        if not root:
            return 0

        queue = deque([(root, 1)])  # Queue of (node, depth) pairs

        while queue:
            node, depth = queue.popleft()
            # Check if it's a leaf node
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

    # Helper function to build a binary tree from list
    def buildTree(values, index=0):
        if index < len(values) and values[index] is not None:
            node = TreeNode(values[index])
            node.left = buildTree(values, 2 * index + 1)
            node.right = buildTree(values, 2 * index + 2)
            return node
        return None
