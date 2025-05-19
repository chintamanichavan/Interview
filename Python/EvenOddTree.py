# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        level = 0  # Starting from level 0

        while queue:
            level_size = len(queue)
            prev_val = None  # To keep track of the previous value in the level

            for _ in range(level_size):
                node = queue.popleft()
                # Check for even/odd values based on level
                if level % 2 == 0 and (node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val)):
                    return False
                if level % 2 == 1 and (node.val % 2 != 0 or (prev_val is not None and node.val >= prev_val)):
                    return False
                prev_val = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return True
