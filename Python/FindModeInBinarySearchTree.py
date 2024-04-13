# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        # Variables to track the current value, count, and max count
        self.prev_val = None
        self.curr_count = 0
        self.max_count = 0
        self.modes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            
            # If the current value is the same as the previous value
            if self.prev_val == node.val:
                self.curr_count += 1
            else:
                self.curr_count = 1

            # If the current count is greater than the max count, clear the modes and add the current value
            if self.curr_count > self.max_count:
                self.modes = [node.val]
                self.max_count = self.curr_count
            # If the current count is equal to the max count, add the current value to the modes
            elif self.curr_count == self.max_count:
                self.modes.append(node.val)
            
            self.prev_val = node.val
            inorder(node.right)

        inorder(root)
        return self.modes
