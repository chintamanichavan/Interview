# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val, root, None)
            return new_root

        queue = [root]
        current_depth = 1

        # Move to the level just before the depth where new nodes will be added
        while current_depth < depth - 1:
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
            current_depth += 1

        # Modify nodes at current depth
        for node in queue:
            new_left = TreeNode(val, node.left, None)
            new_right = TreeNode(val, None, node.right)
            node.left = new_left
            node.right = new_right

        return root

